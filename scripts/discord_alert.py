import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_alert(report):

    discord_message = f"""
🚨 SOC ALERT 🚨

Incident ID: {report['incident_id']}
Severity: {report['severity']}
Host: {report['affected_host']}
IOC: {report['ioc']}

Technique:
{report['mitre_attack']['technique_id']} - {report['mitre_attack']['technique_name']}

Recommendation:
{report['recommendation']}
"""

    try:

        response = requests.post(
            DISCORD_WEBHOOK_URL,
            json={"content": discord_message}
        )

        print("\n===== DISCORD ALERT STATUS =====")
        print(response.status_code)

    except Exception as e:

        print("Discord notification failed")
        print(str(e))
