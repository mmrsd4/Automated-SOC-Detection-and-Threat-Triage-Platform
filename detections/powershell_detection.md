# Encoded PowerShell Detection

## Detection Purpose

Detect suspicious encoded PowerShell execution commonly used in malware and post-exploitation activity.

---

# SPL Query

```spl
EncodedCommand
```

---

# Detection Logic

- Searches for encoded PowerShell execution
- Detects suspicious PowerShell arguments
- Identifies possible attacker activity

---

# Severity

High

---

# MITRE ATT&CK

T1059.001 — PowerShell

---

# Expected Logs

- Sysmon Event ID 1
- PowerShell Operational Logs

---

# Possible False Positives

- Administrative automation scripts
- Legitimate encoded scripts