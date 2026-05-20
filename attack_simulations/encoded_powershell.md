\# Encoded PowerShell Simulation



\## Machine Used



Windows 10



\---



\# Purpose



Generate suspicious endpoint telemetry.



\---



\# Command Used



```powershell

powershell -EncodedCommand SQBuAHYAbwBrAGUALQBF...

```



\---



\# Expected Outcome



\- Sysmon process creation logs generated

\- PowerShell telemetry generated

\- Splunk detection triggered



\---



\# Generated Logs



\- Sysmon Event ID 1

\- PowerShell Operational Logs



\---



\# MITRE ATT\&CK



T1059.001 — PowerShell

