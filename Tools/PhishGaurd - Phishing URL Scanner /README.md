# 🛡️ PhishGuard v1.0

PhishGuard is a Python-based tool designed to help detect potential phishing URLs by analyzing various factors such as SSL certificates, domain similarity, and more. This tool aims to provide a comprehensive check against phishing attacks, making it easier for users to verify the legitimacy of a URL.

## 🎯 Features

- **🔒 SSL Certificate Validation**: Checks if the SSL certificate is valid and matches the domain.
- **🔍 Domain Similarity Check**: Compares the URL's domain with known trusted domains using Levenshtein distance.
- **⚠️ Phishing Domain Detection**: Compares the URL against a list of known phishing domains.
- **⏳ Domain Age Check**: Checks the age of the domain to identify newly registered domains, which are often used in phishing attacks.
- **🔗 Suspicious Pattern Detection**: Analyzes the URL for uncommon TLDs and suspicious patterns.
- **🤖 Automatic Scheme Handling**: If a URL is missing `http://` or `https://`, the tool will prompt the user to add it or test with both.

## 📂 Folder Structure and Files

The tool is organized in the following way:

- **[`src/`](https://github.com/LuciferAsh98/CybersecurityProjects/tree/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/)**: The main directory containing the Python scripts and data.
  - **[`phishguard.py`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/phishguard.py)**: The main script to run the phishing URL scanner.
  - **[`phishing_check.py`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/phishing_check.py)**: Contains the core logic for checking if a URL is potentially phishing.
  - **[`utils.py`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/utils.py)**: Utility functions to support the main scripts.
  - **[`merge_domain_lists.py`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/merge_domain_lists.py)**: Script to merge and process domain lists.
  - **[`requirements.txt`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/requirements.txt)**: Lists the Python packages required to run PhishGuard.
  - **[`data/`](https://github.com/LuciferAsh98/CybersecurityProjects/tree/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/data/)**: Directory containing the domain lists used for checking URLs.
    - **[`phishing_domains.txt`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/data/phishing_domains.txt)**: A list of known phishing domains.
    - **[`compromised_domains_full.txt`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/data/compromised_domains_full.txt)**: A more extensive list of compromised domains.
    - **[`compromised_domains_live.txt`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/data/compromised_domains_live.txt)**: Live list of compromised domains.
    - **[`consolidated_phishing_domains.txt`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/data/consolidated_phishing_domains.txt)**: A consolidated list of phishing domains used by the tool.
    - **[`majestic_million.csv`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/data/majestic_million.csv)**: A CSV file from Majestic Million containing top-ranked domains used for whitelist comparison.
    - **[`top-1m.csv`](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/src/data/top-1m.csv)**: A CSV file containing the top 1 million domains from the Tranco list.


## 🛠️ Installation

To install and run PhishGuard, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/LuciferAsh98/CybersecurityProjects.git
    cd CybersecurityProjects/Tools/PhishGuard - Phishing URL Scanner
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

## 🚀 Usage

To use PhishGuard, simply run the `phishguard.py` script:

```bash
python3 src/phishguard.py


## ✅ Example-Usage
```
PhishGuard v1.0 - Your personal phishing protection tool.

🔍 Enter a URL to check (or type 'q' to quit): youtube.com/
The URL seems to be missing 'http://' or 'https://' .
Would you like to add 'http://' or 'https://' to the URL? (type 'http' or 'https' or 'none' if it doesn’t have !!): https
Checking domain: youtube.com
SSL Certificate SANs include the domain. The certificate is valid.
✅ The URL is safe.
```


## 📜 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/LuciferAsh98/CybersecurityProjects/blob/main/Tools/PhishGaurd%20-%20Phishing%20URL%20Scanner%20/LICENSE.txt) file for details.
