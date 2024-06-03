# Phishing Incident Response Playbook

## Frameworks Used: NIST CSF, ISO/IEC 27001

### 1. Detection

#### 1.1 Monitor Email Security Gateways
- **Description**: Utilize email filtering and security solutions to identify and block suspicious emails.
- **Framework References**: 
  - **NIST CSF**: DE.CM-7
  - **ISO/IEC 27001**: A.12.4.1

#### 1.2 User Reports
- **Description**: Encourage users to report any suspicious email activity through a centralized reporting mechanism.
- **Framework References**:
  - **NIST CSF**: DE.DP-5
  - **ISO/IEC 27001**: A.7.2.2

### 2. Containment

#### 2.1 Block Sender's Email Address
- **Description**: Prevent further phishing emails from the identified malicious source.
- **Framework References**:
  - **NIST CSF**: DE.CM-1
  - **ISO/IEC 27001**: A.12.6.1

#### 2.2 Isolate Affected Systems
- **Description**: Disconnect compromised systems from the network to prevent further spread of the phishing attack.
- **Framework References**:
  - **NIST CSF**: RS.CO-3
  - **ISO/IEC 27001**: A.13.1.3

### 3. Eradication

#### 3.1 Remove Phishing Emails
- **Description**: Delete phishing emails from all user mailboxes to prevent further exposure.
- **Framework References**:
  - **NIST CSF**: RS.MI-3
  - **ISO/IEC 27001**: A.12.6.2

#### 3.2 Scan and Clean Systems
- **Description**: Use antivirus and antimalware tools to clean affected systems.
- **Framework References**:
  - **NIST CSF**: PR.IP-12
  - **ISO/IEC 27001**: A.12.2.1

### 4. Recovery

#### 4.1 Restore Systems from Backups
- **Description**: Use clean backups to restore systems affected by the phishing attack.
- **Framework References**:
  - **NIST CSF**: PR.IP-4
  - **ISO/IEC 27001**: A.12.3.1

#### 4.2 Monitor for Re-infection
- **Description**: Keep an eye on restored systems for any signs of re-infection.
- **Framework References**:
  - **NIST CSF**: RS.CO-2
  - **ISO/IEC 27001**: A.12.4.1

### 5. Lessons Learned

#### 5.1 Post-Incident Analysis
- **Description**: Conduct a thorough analysis of the phishing incident to understand its root cause.
- **Framework References**:
  - **NIST CSF**: PR.IP-10
  - **ISO/IEC 27001**: A.16.1.6

#### 5.2 Update Security Awareness Training
- **Description**: Enhance training programs based on the findings from the phishing incident.
- **Framework References**:
  - **NIST CSF**: PR.AT-5
  - **ISO/IEC 27001**: A.7.2.2
