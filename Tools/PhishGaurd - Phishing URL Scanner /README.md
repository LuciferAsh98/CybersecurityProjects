# 🛡️ PhishGuard v1.0

PhishGuard is a Python-based tool designed to detect potential phishing URLs by analyzing various factors such as SSL certificates, domain similarity, and more. This tool provides a comprehensive check against phishing attacks, making it easier for users to verify the legitimacy of a URL. Stay safe online with PhishGuard!

## ✨ Features

- **🔒 SSL Certificate Validation**: Ensures the SSL certificate is valid and matches the domain, including SAN (Subject Alternative Name) checks.
- **🔍 Domain Similarity Check**: Utilizes Levenshtein distance to compare the URL's domain with known trusted domains to detect suspicious similarities.
- **🚨 Phishing Domain Detection**: Cross-references the URL against a list of known phishing domains to identify potentially dangerous sites.
- **🕒 Domain Age Check**: Verifies the age of the domain to flag newly registered domains, often used in phishing scams.
- **⚠️ Suspicious Pattern Detection**: Analyzes the URL for uncommon TLDs and other suspicious patterns often associated with phishing sites.
- **🔧 Automatic Scheme Handling**: If a URL is missing `http://` or `https://`, the tool prompts the user to add it or tests with both schemes.

## 🚀 Installation

To install and run PhishGuard, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/LuciferAsh98/CybersecurityProjects/tree/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20
    cd CybersecurityProjects/Tools/PhishGuard%20-%20Phishing%20URL%20Scanner%20
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

## 🛠️ Usage

To use PhishGuard, simply run the `phishguard.py` script:

```bash
python3 src/phishguard.py

## ✅ Example-Usage
PhishGuard v1.0 - Your personal phishing protection tool.

🔍 Enter a URL to check (or type 'q' to quit): youtube.com/
The URL seems to be missing 'http://' or 'https://' .
Would you like to add 'http://' or 'https://' to the URL? (type 'http' or 'https' or 'none' if it doesn’t have !!): https
Checking domain: youtube.com
SSL Certificate SANs include the domain. The certificate is valid.
✅ The URL is safe.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.