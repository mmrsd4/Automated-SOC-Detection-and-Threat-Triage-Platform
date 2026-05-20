# PowerShell Monitoring Dashboard

## Purpose

Monitor suspicious PowerShell activity across Windows endpoints.

---

# SPL Query

```spl
powershell
| stats count by host
```

---

# Dashboard Features

- Encoded PowerShell visibility
- Host-based PowerShell monitoring
- Suspicious script execution analysis