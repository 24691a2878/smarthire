import PyPDF2
import re

def extract_text_from_pdf(pdf_file):
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except:
        return ""

def analyze_resume(pdf_file):
    text = extract_text_from_pdf(pdf_file)
    text_lower = text.lower()
    
    keywords = ['python', 'java', 'sql', 'machine learning', 'django', 'javascript', 'html', 'css', 'react', 'node', 'aws', 'git', 'api', 'data', 'project', 'internship']
    
    score = 0
    found = 0
    for kw in keywords:
        if kw in text_lower:
            found += 1
    
    score = 40 + (found * 4)
    if len(text) > 500:
        score += 10
    
    if score > 95:
        score = 89.5
    
    if score < 30:
        score = 58.0
        
    status = "Selected" if score >= 50 else "Not Selected"
    
    return round(score, 2), status