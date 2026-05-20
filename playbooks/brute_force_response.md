\# Brute Force Incident Response Playbook



\## Objective

Detect, investigate, and respond to brute-force authentication attempts detected within the SOC environment.



\---



\# Detection Source



Platform:

\- Splunk Enterprise

\- Windows Security Logs

\- Sysmon

\- Wazuh



Relevant Event IDs:

\- 4625 (Failed Logon)

\- 4624 (Successful Logon)



Detection Query:



```spl

index=main EventCode=4625

| stats count by Account\_Name, Source\_Network\_Address

| sort - count

```



\---



\# Investigation Steps



\## 1. Validate Alert

\- Confirm repeated failed login attempts.

\- Identify targeted user accounts.

\- Identify source IP address.



\## 2. Analyze Login Patterns

Check:

\- Login frequency

\- Authentication time range

\- Multiple account targeting

\- External vs internal IPs



\## 3. Review Endpoint Activity

Investigate:

\- PowerShell execution

\- Suspicious processes

\- Lateral movement indicators



\## 4. Threat Intelligence Enrichment

Enrich source IP using:

\- VirusTotal API

\- AbuseIPDB API



\## 5. Severity Classification



| Severity | Criteria |

| Low | Small number of failed logins |

| Medium | Multiple account targeting |

| High | Successful login after brute force |

| Critical | Privileged account compromise |



\---



\# Containment Actions



\- Block malicious IP

\- Disable compromised account

\- Reset passwords

\- Enable account lockout policy



\---



\# MITRE ATT\&CK Mapping



| Technique | ID |

| Brute Force | T1110 |

| Valid Accounts | T1078 |



\---



\# Lessons Learned



\- Tune alert thresholds

\- Improve password policy

\- Monitor authentication anomalies

\- Enable MFA where possible

