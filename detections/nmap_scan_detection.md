# Nmap Reconnaissance Detection

## Detection Purpose

Detect reconnaissance and network scanning activity against Windows endpoints.

---

# SPL Query

```spl
EventCode=3
| stats count by SourceIp
| where count > 50
```

---

# Detection Logic

- Detects excessive network connections
- Identifies port scanning activity
- Detects reconnaissance behavior

---

# Severity

Low

---

# MITRE ATT&CK

T1046 — Network Service Discovery

---

# Expected Logs

- Sysmon Event ID 3
- Network connection logs

---

# Possible False Positives

- Vulnerability scanners
- Internal IT scans