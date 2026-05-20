# Failed Login Dashboard

## Purpose

Monitor Windows authentication failures and brute-force activity.

---

# SPL Query

```spl
EventCode=4625
| stats count by src_ip
```

---

# Dashboard Features

- Failed login count
- Source IP visibility
- Authentication spike analysis