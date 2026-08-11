from fastapi import FastAPI, UploadFile, Form, File
from fastapi.middleware.cors import CORSMiddleware
from matcher import clean_text
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import io

app = FastAPI(title="Resume Matcher API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text_from_upload(file_bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + " "
    return text

@app.post("/match/")
async def match_resume(
    # Text uses Form
    job_description: str = Form(...), 
    # Files MUST use File
    resume: UploadFile = File(...)
):
    file_bytes = await resume.read()
    raw_resume = extract_text_from_upload(file_bytes)
    
    cleaned_resume = clean_text(raw_resume)
    cleaned_jd = clean_text(job_description)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([cleaned_jd, cleaned_resume])
    match_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    return {
        "filename": resume.filename,
        "match_percentage": round(match_score * 100, 2)
    }