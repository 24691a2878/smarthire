import datetime

def send_selection_email(to_email, candidate_name, score):
    body = f"Hi {candidate_name}, Your resume scored {score}% - Shortlisted for Python Developer at VisionQuest Solutions. Date: {datetime.datetime.now()}"
    print(f"[AUTOMATION] Email to {to_email}: {body}")
    return True

def daily_report_automation(results):
    filename = f"daily_report_{datetime.date.today()}.csv"
    with open(filename, "w") as f:
        f.write("candidate,score,status\n")
        for r in results:
            f.write(f"{r['name']},{r['score']},{r['status']}\n")
    print(f"[AUTOMATION] Report: {filename}")
    return filename