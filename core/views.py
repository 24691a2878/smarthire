from django.shortcuts import render
from .ml_model import analyze_resume
from .automation import send_email_simulation, generate_daily_report

def home(request):
    result = None
    logs = []
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume_file = request.FILES.get('resume')
        if resume_file:
            score, status = analyze_resume(resume_file)
            logs.append(f"[ML] Analysis for {name}: {score}% - {status}")
            send_email_simulation(email, name, status)
            logs.append(f"[AUTOMATION] Email sent to {email}")
            report_path = generate_daily_report(name, email, score, status)
            logs.append(f"[AUTOMATION] Report: {report_path}")
            result = {'name': name, 'email': email, 'score': score, 'status': status}
    return render(request, 'index.html', {'result': result, 'logs': logs})