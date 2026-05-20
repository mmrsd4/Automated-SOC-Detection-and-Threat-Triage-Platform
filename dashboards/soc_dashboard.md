# SOC Dashboard

## Dashboard Purpose

Centralized monitoring dashboard for:
- Authentication events
- Endpoint telemetry
- PowerShell activity
- Reconnaissance activity
- Alert monitoring

---

# Dashboard Panels

## Failed Login Monitoring

```spl
EventCode=4625
| stats count by Account_Name
```

---

## PowerShell Activity

```spl
powershell
| stats count by host
```

---

## Recon Activity

```spl
EventCode=3
| stats count by SourceIp
```

---

# Dashboard Outcome

Provides centralized SOC visibility for:
- Attack monitoring
- Threat investigations
- Endpoint analysis