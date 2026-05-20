# SMB Brute Force Detection

## Detection Purpose

Detect repeated failed login attempts targeting Windows systems.

---

# SPL Query

```spl
EventCode=4625
| stats count by src_ip
| where count > 10
```

---

# Detection Logic

- Monitors Windows failed authentication events
- Detects excessive failed login attempts
- Identifies possible brute-force attacks

---

# Severity

Medium

---

# MITRE ATT&CK

T1110 — Brute Force

---

# Expected Logs

- Windows Security Logs
- Event ID 4625

---

# Possible False Positives

- User typing wrong password repeatedly
- Misconfigured scripts