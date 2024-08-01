import os

def load_domains(file_path):
    with open(file_path, 'r') as file:
        domains = set(line.strip() for line in file)
    return domains

def save_domains(domains, output_file):
    with open(output_file, 'w') as file:
        for domain in sorted(domains):
            file.write(f"{domain}\n")

def main():
    # Define paths to your files
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_domains_path = os.path.join(base_dir, 'data/compromised_domains_full.txt')
    live_domains_path = os.path.join(base_dir, 'data/compromised_domains_live.txt')
    phishing_domains_path = os.path.join(base_dir, 'data/phishing_domains.txt')

    # Load domains from all sources
    full_domains = load_domains(full_domains_path)
    live_domains = load_domains(live_domains_path)
    phishing_domains = load_domains(phishing_domains_path)

    # Combine all domains into a single set (to remove duplicates)
    all_domains = full_domains | live_domains | phishing_domains

    # Save the consolidated list
    output_file_path = os.path.join(base_dir, 'data/consolidated_phishing_domains.txt')
    save_domains(all_domains, output_file_path)
    print(f"Consolidated {len(all_domains)} domains into 'data/consolidated_phishing_domains.txt'.")

if __name__ == "__main__":
    main()
