\# Nmap Reconnaissance Simulation



\## Machine Used



Kali Linux



\---



\# Purpose



Simulate attacker reconnaissance activity.



\---



\# Command Used



```bash

nmap -sV <Windows-IP>

```



\---



\# Expected Outcome



\- Open ports discovered

\- Windows network telemetry generated

\- Recon activity detected in Splunk



\---



\# Generated Logs



\- Sysmon Event ID 3

\- Network connection logs



\---



\# MITRE ATT\&CK



T1046 — Network Service Discovery

