\# Network Architecture



\## Infrastructure Overview



The project environment consists of three virtual machines configured inside VMware Workstation using NAT networking.



| Machine | Purpose |

| Ubuntu Server | SOC Server |

| Windows 10 | Victim Endpoint |

| Kali Linux | Attacker |



\---



\# Attack \& Monitoring Flow



Kali Linux performs attacks against the Windows 10 endpoint.



Windows generates:

\- Security Event Logs

\- Sysmon logs

\- PowerShell logs



Logs are forwarded to:

\- Splunk Enterprise

\- Wazuh Manager



Python automation performs:

\- IOC enrichment

\- Severity scoring

\- Incident report generation

\- Discord notifications



\---



\# Data Flow



Kali Linux

↓

Windows Endpoint

↓

Splunk Universal Forwarder

↓

Ubuntu SOC Server

↓

Splunk Detection Rules

↓

Python Automation

↓

Threat Intelligence APIs

↓

Incident Reports \& Alerts

