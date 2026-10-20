import os
import csv
from datetime import datetime

def send_email_simulation(to_email, name, status):
    print(f"[AUTOMATION] Email sent to {to_email} - {name} is {status}")
    return True

def generate_daily_report(name, email, score, status):
    os.makedirs("daily_reports", exist_ok=True)
    filename = f"daily_reports/report_{datetime.now().strftime('%d-%m-%Y')}.csv"
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Name', 'Email', 'Score', 'Status', 'Date'])
        writer.writerow([name, email, f"{score}%", status, datetime.now().strftime('%d-%m-%Y %H:%M')])
    
    print(f"[AUTOMATION] Daily report generated: {filename}")
    return filename