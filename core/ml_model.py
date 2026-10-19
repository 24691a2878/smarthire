import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import PyPDF2

TRAINING_DATA = {
    'text': [
        "python django machine learning backend developer",
        "python flask api automation",
        "java spring boot developer",
        "python data science pandas scikit learn",
        "hr manager recruitment",
        "sales marketing",
        "python django rest framework ml",
        "accountant tally",
        "python developer django ml automation"
    ],
    'label': [1, 1, 0, 1, 0, 0, 1, 0, 1]
}

vectorizer = TfidfVectorizer()
model = LogisticRegression()

def train_model():
    df = pd.DataFrame(TRAINING_DATA)
    X = vectorizer.fit_transform(df['text'])
    model.fit(X, df['label'])
    return model, vectorizer

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()

def predict_resume(pdf_file):
    m, v = train_model()
    text = extract_text_from_pdf(pdf_file)
    if not text:
        return 0, 0
    score = v.transform([text])
    pred = m.predict(score)[0]
    prob = m.predict_proba(score)[0][1] * 100
    return pred, round(prob, 2)