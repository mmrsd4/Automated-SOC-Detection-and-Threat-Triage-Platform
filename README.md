# Automated SOC Detection & Threat Triage Platform

## Overview

This project simulates an enterprise-style Security Operations Center (SOC) environment focused on centralized log collection, attack detection, automated threat triage, and incident response workflows.

The lab integrates:
- Splunk Enterprise
- Wazuh
- Sysmon
- Python automation
- VirusTotal API
- AbuseIPDB API

The environment was designed to simulate real-world SOC operations including:
- Endpoint telemetry monitoring
- Detection engineering
- Attack simulation
- IOC enrichment
- Alert triage
- Incident reporting
- Threat intelligence integration

---

# Lab Environment

| System | Role |
| Ubuntu Server | Central SOC Server |
| Windows 10 | Monitored Endpoint |
| Kali Linux | Attack Simulation System |

---

# Technology Stack

| Category | Tools |
| SIEM | Splunk Enterprise |
| Endpoint Monitoring | Sysmon |
| Security Monitoring | Wazuh |
| Log Forwarding | Splunk Universal Forwarder |
| Automation | Python |
| Threat Intelligence | VirusTotal API, AbuseIPDB API |
| Operating Systems | Ubuntu Server, Windows 10, Kali Linux |

---

# SOC Workflow

## 1. Build Lab Environment

### Ubuntu Server
![Ubuntu](screenshots/ubuntu/1-ubuntu-ip.png)

### Windows Endpoint
![Windows](screenshots/windows/3-windows-ip.png)

### Kali Linux
![Kali](screenshots/kali/6-kali-ip.png)

---

# 2. Central SOC Server Configuration

## Splunk Enterprise Operational
![Splunk](screenshots/splunk/2-splunkenterprice-working.png)

---

# 3. Windows Endpoint Telemetry Collection

## Sysmon Logs Generated
![Sysmon](screenshots/windows/4-sysmonlogs.png)

## Windows Logs Forwarded to Splunk
![Windows Logs](screenshots/splunk/5-Windowslogs-generated-in-splunk.png)

---

# 4. Attack Simulation

## Nmap Reconnaissance Scan
![Nmap](screenshots/kali/7-Nmap-results.png)

## Splunk Detection for Nmap Activity
![Nmap Detection](screenshots/splunk/8-Splunk-nmap-detection.png)

---

## Hydra SMB Brute Force Attack
![Hydra](screenshots/kali/9-Hydra-attack.png)

## Failed Login Events Detected
![Failed Logins](screenshots/splunk/10-failed-login-events-of-hydra.png)

## Failed Login SPL Query Results
![SPL Query](screenshots/splunk/13-failed-login-SPL-query-results.png)

## Failed Login Alert Creation
![Alert](screenshots/splunk/14-failed-login-Alert-creation-page.png)

---

## Suspicious PowerShell Execution
![PowerShell](screenshots/windows/11-PowerShell-execution.png)

## Splunk PowerShell Detection
![PowerShell Detection](screenshots/splunk/12-PowerShell-execution-Splunk-detection.png)

## Encoded Command Alert Detection
![Encoded Alert](screenshots/splunk/15-encoded-command-alert.png)

---

# 5. SOC Dashboard & Alerting

## Full SOC Dashboard
![SOC Dashboard](screenshots/splunk/17-full-SOC-dashboard.png)

## Splunk Alert Configuration
![Splunk Alerts](screenshots/splunk/18-Configure-Splunk-Alerts.png)

---

# 6. Wazuh Security Monitoring

## Active Wazuh Agent
![Wazuh Agent](screenshots/wazuh/19-active-Wazuh-agent.png)

## Wazuh Dashboard
![Wazuh Dashboard](screenshots/wazuh/20-Wazuh-dashboard.png)

## Wazuh Security Event
![Wazuh Event](screenshots/wazuh/21-Wazuh-event.png)

---

# 7. Automated IOC Enrichment & Threat Triage

## Python IOC Enrichment Automation
![IOC Automation](screenshots/automation/16-Python-IOC-Enrichment-Automation.png)

## IOC Enrichment Results
![IOC Results](screenshots/automation/22-Python%20IOC-Enrichment-Script-terminal-output-and%20IOC-Enrichment-Result.png)

## JSON Incident Report Generation
![JSON Report](screenshots/automation/23-Python-IOC-Enrichment-Script-JSON-Incident-Report.png)

## Automated Incident Reports
![Incident Report](screenshots/automation/24-Generate-Automated-Incident-Reports.png)

## Discord Alert Notifications
![Discord Alerts](screenshots/automation/25-Discord-Alert-Notifications-.png)

## Incident Report with MITRE ATT&CK IDs
![ATTACK Mapping](screenshots/automation/26-Incident-Report-with-ATT&CK-IDs.png)

---

# Detection Engineering

## Key Detection Use Cases

### Brute Force Detection
- Windows Event ID 4625
- Authentication anomaly monitoring
- Failed login threshold alerts

### PowerShell Abuse Detection
- Encoded PowerShell commands
- Suspicious process execution
- Process creation monitoring

### Reconnaissance Detection
- Nmap scan activity
- Port scan behavior analysis
- Network telemetry investigation

---

# Automation Features

## IOC Enrichment Pipeline

Integrated APIs:
- VirusTotal
- AbuseIPDB

Automation capabilities:
- IOC reputation analysis
- Threat severity classification
- Automated JSON reporting
- Discord notifications
- Incident enrichment workflows

---

# MITRE ATT&CK Mapping

| Technique | ATT&CK ID |
| PowerShell | T1059.001 |
| Brute Force | T1110 |
| Network Service Scanning | T1046 |
| Command and Scripting Interpreter | T1059 |

---

# Project Structure

```text
Automated-SOC-Platform/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── architecture/
├── detections/
├── dashboards/
├── attack_simulations/
├── automation/
├── playbooks/
├── rules/
├── scripts/
├── reports/
├── screenshots/
└── mitre_mapping/
```

---

# Detection Query Example

```spl
index=main EventCode=4625
| stats count by Account_Name, Source_Network_Address
| where count > 5
```


---

# Disclaimer

This project was built in an isolated lab environment for educational and defensive cybersecurity purposes only.

---

# License

This project is licensed under the MIT License.
