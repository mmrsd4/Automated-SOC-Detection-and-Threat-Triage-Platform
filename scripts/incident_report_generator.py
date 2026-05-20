import json
import os
from datetime import datetime

def generate_incident_report(report):

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"reports/ioc_report_{report['ioc'].replace('.', '_')}_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print("\n===== FINAL INCIDENT REPORT =====")
    print(json.dumps(report, indent=4))

    print(f"\nReport saved to: {filename}")
