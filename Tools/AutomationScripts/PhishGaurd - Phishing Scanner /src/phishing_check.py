import os
import ssl
import socket
import re
import whois
import pandas as pd
from datetime import datetime
from urllib.parse import urlparse
from colorama import Fore
from Levenshtein import distance as levenshtein_distance

# Load the consolidated phishing domains list
base_dir = os.path.dirname(os.path.abspath(__file__))
consolidated_domains_path = os.path.join(base_dir, 'data/consolidated_phishing_domains.txt')

with open(consolidated_domains_path) as f:
    PHISHING_DOMAINS = set(line.strip() for line in f)

# Load the whitelist domains from Majestic Million and Tranco top-1m
majestic_path = os.path.join(base_dir, 'data/majestic_million.csv')
tranco_path = os.path.join(base_dir, 'data/top-1m.csv')

majestic_df = pd.read_csv(majestic_path)
tranco_df = pd.read_csv(tranco_path, header=None, names=["Rank", "Domain"])

WHITELIST_DOMAINS = set(majestic_df['Domain'].str.lower().tolist() + tranco_df['Domain'].str.lower().tolist())

# List of uncommon TLDs often used in phishing
UNCOMMON_TLDS = {'.pro', '.xyz', '.top', '.online', '.club', '.site', '.info', '.biz'}

# Threshold for domain similarity
SIMILARITY_THRESHOLD = 3  # Levenshtein distance threshold

def extract_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain

def is_phishing_url(url):
    # Check if the URL has a scheme (http or https)
    if not url.startswith(('http://', 'https://')):
        print("The URL seems to be missing 'http://' or 'https://' .")
        while True:
            scheme = input("Would you like to add 'http://' or 'https://' to the URL? (type 'http' or 'https' or 'none' if it doesnt have !!): ")
            if scheme.lower() == 'http':
                url = f"http://{url}"
                break
            elif scheme.lower() == 'https':
                url = f"https://{url}"
                break
            elif scheme.lower() == 'none':
                print("Testing with both http:// and https://")
                http_url = f"http://{url}"
                https_url = f"https://{url}"
                
                # Check SSL for both HTTP and HTTPS
                if check_ssl_certificate(https_url, extract_domain(https_url)):
                    print(f"{Fore.GREEN}✅ The URL is safe.")
                    return False  # Safe with HTTPS
                
                if check_ssl_certificate(http_url, extract_domain(http_url)):
                    print(f"{Fore.GREEN}✅ The URL is safe.")
                    return False  # Safe with HTTP
                
                print(f"{Fore.RED}❌ Unable to validate the SSL certificate, further checks will be performed.")
                url = https_url  # Proceed with HTTPS URL for further checks
                break
            else:
                print("Invalid input. Please enter a valid option.")

    # Extract the domain from the URL
    domain = extract_domain(url)
    if not domain:
        print(f"{Fore.RED}Invalid or empty domain extracted. Please check the URL.")
        return True

    print(f"Checking domain: {domain}")

    # Check if the domain is an IP address
    if is_ip_address(domain):
        print(f"{Fore.RED}URL contains an IP address, which is uncommon for legitimate sites.")
        return True

    # Perform SSL certificate analysis first
    ssl_valid = check_ssl_certificate(url, domain)
    if ssl_valid:
        print(f"{Fore.GREEN}✅ The URL is safe.")
        return False  # No need to check against whitelist or similarity if SSL is valid

    # Check if the domain is in the phishing domains list
    if domain in PHISHING_DOMAINS:
        print(f"{Fore.RED}Domain '{domain}' is known to be compromised or involved in phishing.")
        return True
    
    # Perform domain similarity check
    if domain_similarity_check(domain):
        print(f"{Fore.RED}Domain '{domain}' is suspiciously similar to a known brand.")
        return True

    # Perform domain age check
    if domain_age_check(domain):
        print(f"{Fore.RED}Domain '{domain}' is newly registered, which is common in phishing.")
        return True

    # Perform URL pattern heuristic analysis
    if contains_suspicious_patterns(url):
        print(f"{Fore.RED}URL contains suspicious patterns often seen in phishing sites.")
        return True
    
    # If no issues found, return False (indicating URL is safe)
    print(f"{Fore.GREEN}✅ The URL is safe.")
    return False


def is_ip_address(domain):
    # Regular expression for matching IPv4 and IPv6 addresses
    ip_pattern = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$|^[a-fA-F0-9:]+$')
    return bool(ip_pattern.match(domain))

def check_ssl_certificate(url, domain):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        # Connect to the server and get the SSL certificate
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        # Check the common name (CN) in the certificate against the hostname
        common_name = dict(x[0] for x in cert['subject'])['commonName']
        san = cert.get('subjectAltName', [])

        # Extract SAN domains
        san_domains = [san_entry[1] for san_entry in san if san_entry[0] == 'DNS']

        # Validate the domain against SANs
        if common_name == hostname or hostname.endswith(common_name) or any(hostname.endswith(san_domain) for san_domain in san_domains):
            print(f"{Fore.GREEN}SSL Certificate SANs include the domain. The certificate is valid.")
            return True
        else:
            print(f"{Fore.RED}SSL Certificate CN '{common_name}' does not match the domain '{hostname}'.")
            print(f"{Fore.RED}SANs found: {san_domains}")
            return False

    except Exception as e:
        print(f"{Fore.RED}Error during SSL Certificate check: {e}")
        return False


def domain_similarity_check(domain):
    # Check for similarity with known whitelist domains
    for whitelist_domain in WHITELIST_DOMAINS:
        if levenshtein_distance(domain, whitelist_domain) <= SIMILARITY_THRESHOLD:
            print(f"Domain '{domain}' is suspiciously similar to whitelisted domain '{whitelist_domain}'.")
            return True
    
    return False

def domain_age_check(domain):
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date is None:
            raise ValueError("Creation date is None")

        age = (datetime.now() - creation_date).days

        if age < 365:  # Less than a year old
            return True
    except Exception as e:
        print(f"{Fore.RED}Error during domain age check: {e}")
        return False

    return False

def contains_suspicious_patterns(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Check for uncommon TLDs
    tld = '.' + domain.split('.')[-1]
    if tld in UNCOMMON_TLDS:
        return True

    # Check for suspicious patterns like unusual characters, too many hyphens, or strange subdomains
    suspicious_patterns = [
        r"[^a-zA-Z0-9\.\-:/]",  # Unusual characters (excluding standard URL characters)
        r"-{3,}",               # Three or more consecutive hyphens
        r"\.\.",                # Multiple dots in domain
        r"^https?://(\w+\.){4,}",  # More than 3 subdomains (adjust if needed)
    ]
    
    for pattern in suspicious_patterns:
        if re.search(pattern, url):
            return True
    
    return False
