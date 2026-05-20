\# Hydra Brute Force Simulation



\## Machine Used



Kali Linux



\---



\# Purpose



Simulate SMB brute-force authentication attack.



\---



\# Command Used



```bash

hydra -l administrator -P rockyou.txt smb://<Windows-IP>

```



\---



\# Expected Outcome



\- Failed login events generated

\- Event ID 4625 logs generated

\- Splunk alerts triggered



\---



\# Generated Logs



\- Windows Security Event Logs

\- Event ID 4625



\---



\# MITRE ATT\&CK



T1110 — Brute Force

