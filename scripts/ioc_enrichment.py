import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path

from incident_report_generator import generate_incident_report
from discord_alert import send_discord_alert

# ---------------------------------
# Load Environment Variables
# ---------------------------------

env_path = Path(__file__).parent / ".env"

load_dotenv(dotenv_path=env_path)

VT_API_KEY = os.getenv("VT_API_KEY")
ABUSE_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

# ---------------------------------
# IOC + ATTACK TYPE
# ---------------------------------

ioc_ip = "8.8.8.8"

attack_type = "Brute Force"

# ---------------------------------
# MITRE ATT&CK Mapping
# ---------------------------------

mitre_mapping = {

    "Brute Force": {
        "technique_id": "T1110",
        "technique_name": "Brute Force"
    },

    "PowerShell Abuse": {
        "technique_id": "T1059.001",
        "technique_name": "PowerShell"
    },

    "Network Scanning": {
        "technique_id": "T1046",
        "technique_name": "Network Service Scanning"
    }
}

# ---------------------------------
# Base Incident Report
# ---------------------------------

report = {
    "incident_id": "INC-001",
    "incident_type": attack_type,
    "severity": "Low",
    "timestamp": str(datetime.now()),
    "affected_host": "WIN10",
    "source_of_alert": "Splunk",
    "analyst": "Rashad",
    "ioc": ioc_ip,
    "mitre_attack": mitre_mapping.get(
        attack_type,
        {
            "technique_id": "UNKNOWN",
            "technique_name": "UNKNOWN"
        }
    ),
    "abuseipdb": {},
    "virustotal": {},
    "analyst_notes": "",
    "recommendation": ""
}

# ---------------------------------
# AbuseIPDB Lookup
# ---------------------------------

abuse_headers = {
    "Key": ABUSE_API_KEY,
    "Accept": "application/json"
}

abuse_url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ioc_ip}"

abuse_response = requests.get(abuse_url, headers=abuse_headers)

print("\n===== ABUSEIPDB STATUS =====")
print(abuse_response.status_code)

abuse_data = abuse_response.json()

if "data" in abuse_data:

    report["abuseipdb"] = {
        "abuseConfidenceScore": abuse_data["data"]["abuseConfidenceScore"],
        "countryCode": abuse_data["data"]["countryCode"],
        "isp": abuse_data["data"]["isp"]
    }

# ---------------------------------
# VirusTotal Lookup
# ---------------------------------

vt_headers = {
    "x-apikey": VT_API_KEY
}

vt_url = f"https://www.virustotal.com/api/v3/ip_addresses/{ioc_ip}"

vt_response = requests.get(vt_url, headers=vt_headers)

print("\n===== VIRUSTOTAL STATUS =====")
print(vt_response.status_code)

vt_data = vt_response.json()

if "data" in vt_data:

    stats = vt_data["data"]["attributes"]["last_analysis_stats"]

    report["virustotal"] = {
        "malicious_votes": stats["malicious"],
        "suspicious_votes": stats["suspicious"],
        "harmless_votes": stats["harmless"]
    }

# ---------------------------------
# Severity Logic
# ---------------------------------

if report["abuseipdb"].get("abuseConfidenceScore", 0) > 80:
    report["severity"] = "High"

if report["virustotal"].get("malicious_votes", 0) > 5:
    report["severity"] = "Critical"

# ---------------------------------
# Analyst Notes
# ---------------------------------

if report["severity"] == "Critical":

    report["analyst_notes"] = "IOC appears malicious."

    report["recommendation"] = "Immediate investigation required."

else:

    report["analyst_notes"] = "IOC currently appears non-malicious."

    report["recommendation"] = "No immediate malicious activity detected."

# ---------------------------------
# Generate Report
# ---------------------------------

generate_incident_report(report)

# ---------------------------------
# Send Discord Alert
# ---------------------------------

send_discord_alert(report)
