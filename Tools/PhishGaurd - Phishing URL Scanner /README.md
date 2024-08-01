# PhishGuard v1.0

PhishGuard is a Python-based tool designed to help detect potential phishing URLs by analyzing various factors such as SSL certificates, domain similarity, and more. This tool aims to provide a comprehensive check against phishing attacks, making it easier for users to verify the legitimacy of a URL.

## Features

- **SSL Certificate Validation**: Checks if the SSL certificate is valid and matches the domain.
- **Domain Similarity Check**: Compares the URL's domain with known trusted domains using Levenshtein distance.
- **Phishing Domain Detection**: Compares the URL against a list of known phishing domains.
- **Domain Age Check**: Checks the age of the domain to identify newly registered domains, which are often used in phishing attacks.
- **Suspicious Pattern Detection**: Analyzes the URL for uncommon TLDs and suspicious patterns.
- **Automatic Scheme Handling**: If a URL is missing `http://` or `https://`, the tool will prompt the user to add it or test with both.

## Installation

To install and run PhishGuard, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/PhishGuard.git
    cd PhishGuard
    ```

2. **Set up a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use PhishGuard, simply run the `phishguard.py` script:

```bash
python3 src/phishguard.py
