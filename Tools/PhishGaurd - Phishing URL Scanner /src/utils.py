# Example of a utility function if you need it
def extract_domain(url):
    # Function to extract domain from a URL
    from urllib.parse import urlparse
    domain = urlparse(url).netloc
    return domain
