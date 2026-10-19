from django.shortcuts import render
from .ml_model import predict_resume
from .automation import send_selection_email, daily_report_automation

def home(request):
    result = None
    if request.method == 'POST' and request.FILES.get('resume'):
        pdf_file = request.FILES['resume']
        name = request.POST.get('name', 'Candidate')
        email = request.POST.get('email', 'test@test.com')
        
        pred, score = predict_resume(pdf_file)
        
        status = "Selected" if pred == 1 else "Rejected"
        
        # AUTOMATION PART - as per your certificate
        send_selection_email(email, name, score)
        daily_report_automation([{'name': name, 'score': score, 'status': status}])
        
        result = {'name': name, 'email': email, 'score': score, 'status': status}
    
    return render(request, 'index.html', {'result': result})