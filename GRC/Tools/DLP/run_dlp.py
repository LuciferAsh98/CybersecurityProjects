import yaml
import re

def load_config():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def identify_sensitive_data(data, patterns):
    found_data = {}
    for data_type, pattern in patterns.items():
        matches = re.findall(pattern, data)
        if matches:
            found_data[data_type] = matches
    return found_data

def monitor_data(file_path, patterns):
    with open(file_path, 'r') as file:
        data = file.read()
    identified_data = identify_sensitive_data(data, patterns)
    return identified_data

def enforce_policies(identified_data, policy):
    violations = {}
    if policy['enforce_policies']:
        for data_type, data in identified_data.items():
            if data:
                violations[data_type] = data
        if policy['log_violations']:
            log_violations(violations)
    return violations

def log_violations(violations):
    with open('violations.log', 'a') as log_file:
        for data_type, data in violations.items():
            log_file.write(f"Policy violation for {data_type}: {data}\n")

def notify_incident(response_config, violations):
    if response_config['notify_on_breach']:
        subject = "DLP Tool Alert: Policy Violation Detected"
        body = f"The following policy violations were detected:\n\n{violations}"
        recipients = response_config['notification_recipients']
        print(f"Simulated email to: {recipients}\nSubject: {subject}\nBody:\n{body}\n")

def main():
    config = load_config()
    print("DLP Tool is running with the following configuration:")
    print(config)

    # Patterns for identifying sensitive data
    patterns = {
        'credit_card_numbers': r'\b\d{4}-\d{4}-\d{4}-\d{4}\b',
        'social_security_numbers': r'\b\d{3}-\d{2}-\d{4}\b',
        'email_addresses': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    }

    # Monitor data from a sample file
    file_path = 'sample_data.txt'
    identified_data = monitor_data(file_path, patterns)
    print("Identified sensitive data:")
    print(identified_data)

    # Enforce policies based on identified data
    violations = enforce_policies(identified_data, config['policy'])
    if violations:
        print("Policy violations logged.")
        notify_incident(config['incident_response'], violations)

if __name__ == "__main__":
    main()
