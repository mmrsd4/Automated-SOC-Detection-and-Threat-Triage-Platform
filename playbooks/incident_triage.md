\# SOC Incident Triage Workflow



\## Objective

Standardize SOC alert triage and incident handling procedures.



\---



\# Alert Sources



\- Splunk Enterprise

\- Wazuh

\- Sysmon

\- Python IOC Enrichment Pipeline



\---



\# Triage Workflow



\## Step 1 — Alert Validation

Validate:

\- Alert legitimacy

\- Trigger conditions

\- False positives



\## Step 2 — Initial Classification



| Severity | Description |

| Low | Informational activity |

| Medium | Suspicious behavior |

| High | Confirmed malicious indicators |

| Critical | Active compromise |



\---



\## Step 3 — IOC Enrichment



Enrichment Sources:

\- VirusTotal

\- AbuseIPDB



Analyze:

\- IP reputation

\- Domain reputation

\- File hashes



\---



\## Step 4 — Incident Correlation



Correlate:

\- Authentication logs

\- Process activity

\- Network activity

\- Endpoint telemetry



\---



\## Step 5 — Escalation



Escalate incidents involving:

\- Privileged accounts

\- Malware execution

\- Remote access activity

\- Lateral movement



\---



\## Step 6 — Reporting



Generate:

\- JSON incident reports

\- Analyst notes

\- ATT\&CK mappings

\- Severity classification



\---



\# SOC Workflow Summary



Attack Activity

↓

Log Collection

↓

Splunk Detection

↓

IOC Enrichment

↓

Severity Assignment

↓

Discord Notification

↓

Incident Report Generation

