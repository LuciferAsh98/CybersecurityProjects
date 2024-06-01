import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Paths and constants
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
EMAIL_TEMPLATE = os.path.join(CURRENT_DIR, "email_template.txt")

# Function to generate and send phishing email
def send_phishing_email():
    logging.info("Sending phishing email...")
    
    # Read email content from the template
    with open(EMAIL_TEMPLATE, "r") as template:
        email_content = template.read()
    
    from_email = os.getenv('EMAIL_USER')
    to_email = "target_email@example.com"  # Replace with the target email
    subject = "Important Update"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(email_content, 'plain'))
    
    try:
        server = smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT'))
        server.starttls()
        server.login(from_email, os.getenv('EMAIL_PASS'))
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        logging.info("Phishing email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_phishing_email()
