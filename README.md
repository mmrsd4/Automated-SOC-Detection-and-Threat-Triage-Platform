\# Automated SOC Detection \& Alert Triage Platform



\## Project Overview



This project simulates a real-world SOC (Security Operations Center) environment for detecting, monitoring, investigating, and triaging security incidents using Splunk, Wazuh, Sysmon, Python automation, and Windows/Linux systems.



The platform was built using multiple virtual machines to simulate enterprise attack and defense workflows.



\---



\# Lab Environment



| Machine | Role |

| Ubuntu Server | SOC Server |

| Windows 10 | Victim Endpoint |

| Kali Linux | Attacker Machine |



\---



\# Tools Used



| Tool | Purpose |

| Splunk Enterprise | SIEM monitoring |

| Wazuh | Endpoint monitoring |

| Sysmon | Windows telemetry |

| Splunk Universal Forwarder | Log forwarding |

| Python | Alert automation |

| Nmap | Reconnaissance |

| Hydra | Brute-force simulation |

| VirusTotal API | IOC enrichment |

| AbuseIPDB | Threat intelligence |



\---



\# Architecture



\- Kali Linux attacks Windows 10 endpoint

\- Windows generates logs

\- Logs are forwarded to Ubuntu SOC Server

\- Splunk detects suspicious activity

\- Python automation enriches alerts

\- Incident reports are generated

\- Discord notifications are sent



\---



\# Network Configuration



All virtual machines use NAT networking inside VMware Workstation.



| Machine | Example IP |

| Ubuntu Server | 192.168.x.x |

| Windows 10 | 192.168.x.x |

| Kali Linux | 192.168.x.x |



\---



\# Project Workflow



\## Step 1 — VM Setup



\- Created Ubuntu Server VM

\- Created Windows 10 VM

\- Created Kali Linux VM

\- Configured NAT networking



\---



\## Step 2 — Splunk Installation



Installed Splunk Enterprise on Ubuntu Server.



Configured:

\- Web interface

\- Receiving port 9997

\- Log indexing



\---



\## Step 3 — Endpoint Monitoring



Installed:

\- Sysmon

\- Splunk Universal Forwarder

\- Wazuh Agent



on Windows 10 endpoint.



\---



\## Step 4 — Attack Simulation



Performed:

\- Nmap reconnaissance

\- SMB brute-force attacks using Hydra

\- Encoded PowerShell execution



from Kali Linux.



\---



\## Step 5 — Detection Engineering



Created SPL detections for:

\- Failed logins

\- Recon activity

\- Encoded PowerShell

\- Endpoint telemetry anomalies



\---



\## Step 6 — Automation



Built Python automation scripts for:

\- IOC enrichment

\- Severity classification

\- Incident report generation

\- Discord alert notifications



\---



\## Step 7 — Reporting \& Documentation



Created:

\- MITRE ATT\&CK mappings

\- Detection documentation

\- Incident reports

\- SOC dashboards



\---



\# Screenshots



\## Ubuntu Server

!\[Ubuntu](screenshots/ubuntu/1-ubuntu-ip.png)



\## Splunk Working

!\[Splunk](screenshots/splunk/2-splunkenterprise-working.png)



\## Windows Endpoint

!\[Windows](screenshots/windows/3-windows-ip.png)



\## Sysmon Logs

!\[Sysmon](screenshots/windows/4-sysmonlogs.png)



\## Windows Logs in Splunk

!\[Splunk Logs](screenshots/splunk/5-Windowslogs-generated-in-splunk.png)



\## Kali Linux

!\[Kali](screenshots/kali/6-kali-ip.png)



\## Nmap Scan

!\[Nmap](screenshots/kali/7-Nmap-results.png)



\## Splunk Nmap Detection

!\[Nmap Detection](screenshots/splunk/8-Splunk-nmap-detection.png)



\## Hydra Brute Force

!\[Hydra](screenshots/kali/9-Hydra-attack.png)



\## Failed Login Events

!\[Failed Logins](screenshots/splunk/10-failed-login-events-of-hydra.png)



\## PowerShell Execution

!\[PowerShell](screenshots/windows/11-PowerShell-execution.png)



\## PowerShell Detection

!\[PowerShell Detection](screenshots/splunk/12-PowerShell-execution-Splunk-detection.png)



\## Failed Login SPL Query

!\[SPL Query](screenshots/splunk/13-failed-login-SPL-query-results.png)



\## Splunk Alert

!\[Alert](screenshots/splunk/14-failed-login-Alert-creation-page.png)



\## Encoded Command Alert

!\[Encoded Alert](screenshots/splunk/15-encoded-command-alert.png)



\## Python IOC Enrichment

!\[IOC Enrichment](screenshots/automation/16-Python-IOC-Enrichment-Automation.png)



\## Full SOC Dashboard

!\[SOC Dashboard](screenshots/splunk/17-full-SOC-dashboard.png)



\## Splunk Alerts

!\[Alerts](screenshots/splunk/18-Configure-Splunk-Alerts.png)



\## Active Wazuh Agent

!\[Wazuh Agent](screenshots/wazuh/19-active-Wazuh-agent.png)



\## Wazuh Dashboard

!\[Wazuh Dashboard](screenshots/wazuh/20-Wazuh-dashboard.png)



\## Wazuh Event

!\[Wazuh Event](screenshots/wazuh/21-Wazuh-event.png)



\## IOC Enrichment Result

!\[IOC Result](screenshots/automation/22-Python-IOC-Enrichment-Script-terminal-output-and-IOC-Enrichment-Result.png)



\## JSON Incident Report

!\[JSON Report](screenshots/automation/23-Python-IOC-Enrichment-Script-JSON-Incident-Report.png)



\## Automated Incident Report

!\[Incident Report](screenshots/automation/24-Generate-Automated-Incident-Reports.png)



\## Discord Alerts

!\[Discord](screenshots/automation/25-Discord-Alert-Notifications.png)



\## Incident Report with ATT\&CK IDs

!\[ATTACK](screenshots/reports/26-Incident-Report-with-ATT\&CK-IDs.png)



\---



\# MITRE ATT\&CK Mapping



| Attack | ATT\&CK Technique |

| SMB Brute Force | T1110 |

| Network Scanning | T1046 |

| PowerShell Abuse | T1059.001 |



\---



\# Project Outcome



This project demonstrates:

\- SIEM monitoring

\- Endpoint telemetry analysis

\- Threat detection

\- Alert triage

\- IOC enrichment

\- Threat intelligence integration

\- Incident reporting

\- MITRE ATT\&CK mapping

\- SOC workflow understanding

