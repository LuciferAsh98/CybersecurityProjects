# Phishing Email Automation

This project demonstrates a simple automation script to generate and send phishing emails using the Social-Engineer Toolkit (SET). It automates the creation of a phishing email campaign and configures SET to run the campaign.

## Table of Contents
- [Files](#files)
- [Pre-requisites](#pre-requisites)
- [Installation](#installation)
- [Usage](#usage)
- [Disclaimer](#disclaimer)

## Files

- **phishing_email_automation.py**: The main script to automate phishing email generation and SET configuration.
- **email_template.txt**: Template for the phishing email content.
- **EnvironmentFile.env**: Environment file to store configuration settings.

## Pre-requisites

1. **Social-Engineer Toolkit (SET)**:
   - Ensure that SET is installed on your system. For installation instructions, visit the [SET repository](https://github.com/trustedsec/social-engineer-toolkit).

2. **Python Packages**:
   - Install the necessary Python packages using the following command:

     pip install -r requirements.txt

3. **Environment Setup**:
   - Create an environment file named `EnvironmentFile.env` and include the following content:
     SUDO_PASSWORD=your_sudo_password
     SET_PATH=/usr/share/set


## Installation

1. **Clone the repository**:
   
   git clone <-repo-url>

2. **Set permissions**:

```bash   
   chmod +x phishing_email_automation.py
```

##Usage

**Execute the main script**
   
```bash
   python3 phishing_email_automation.py
```