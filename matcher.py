import pdfplumber
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download stopwords on first run
nltk.download('stopwords', quiet=True)

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + " "
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text) 
    text = text.lower() 
    stop_words = set(stopwords.words('english'))
    return " ".join([word for word in text.split() if word not in stop_words])

def match_resume_to_jd(resume_path, job_description):
    # 1. Extract
    raw_resume = extract_text_from_pdf(resume_path)
    
    # ADD THIS LINE TO DEBUG:
    print(f"\n--- Extracted Text ---\n{raw_resume}\n----------------------\n")
    
    # 2. Clean
    cleaned_resume = clean_text(raw_resume)
    cleaned_jd = clean_text(job_description)
    
    # 3. Vectorize
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([cleaned_jd, cleaned_resume])
    
    # 4. Score
    match_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(match_score * 100, 2)

# --- Run the Program ---
if __name__ == "__main__":
    # Define the job requirements
    jd = "Looking for a software engineer skilled in Python, machine learning, and NLP."
    
    # Point this to a real PDF in your folder!
    resume_file = "sample_resume.pdf" 
    
    print(f"Analyzing {resume_file}...")
    score = match_resume_to_jd(resume_file, jd)
    print(f"Match Score: {score}%")