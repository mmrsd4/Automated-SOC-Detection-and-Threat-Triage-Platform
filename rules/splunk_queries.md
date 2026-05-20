\# Splunk Detection Queries



\---



\# Failed Login Detection



```spl

index=main EventCode=4625

| stats count by Account\_Name, Source\_Network\_Address

```



\---



\# Successful Login Detection



```spl

index=main EventCode=4624

```



\---



\# PowerShell Detection



```spl

index=main powershell

```



\---



\# Encoded PowerShell Detection



```spl

index=main "\*EncodedCommand\*"

```



\---



\# Sysmon Network Connections



```spl

index=main EventCode=3

```



\---



\# Nmap Reconnaissance Detection



```spl

index=main EventCode=3

| stats count by destination\_port, SourceIp

| sort - count

```



\---



\# Suspicious Process Creation



```spl

index=main EventCode=4688

| table \_time host New\_Process\_Name Process\_Command\_Line

```



\---



\# Failed Login Threshold Detection



```spl

index=main EventCode=4625

| stats count by Source\_Network\_Address

| where count > 5

```

