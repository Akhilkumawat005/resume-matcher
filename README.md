# Resume Matcher 📄🤖

An end-to-end machine learning application that automatically parses and ranks candidate resumes against job descriptions using Natural Language Processing (NLP). 

## 🚀 Overview

Developed an ML-based resume matcher to automate candidate screening. This tool evaluates the semantic similarity between a job description and a candidate's resume, outputting a precise match percentage. It features a RESTful FastAPI backend for the machine learning engine and an interactive Streamlit frontend for ease of use.

## ✨ Features

* **Automated Parsing:** Extracts raw text directly from PDF resumes.
* **NLP Preprocessing:** Cleans text by removing punctuation, standardizing casing, and filtering out English stop-words using NLTK.
* **Semantic Matching:** Utilizes TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to weigh keyword importance.
* **Fit Scoring:** Calculates the Cosine Similarity between the resume and job description vectors to generate a 0-100% fit score.
* **Full-Stack Architecture:** Decoupled backend (FastAPI) and frontend (Streamlit) communicating via REST API.

## 🛠️ Tech Stack

* **Machine Learning & NLP:** `scikit-learn`, `nltk`
* **Backend:** Python, `FastAPI`, `uvicorn`, `python-multipart`
* **Frontend:** `Streamlit`
* **Document Processing:** `pdfplumber`

## 💻 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/Akhilkumawat005/resume-matcher.git](https://github.com/Akhilkumawat005/resume-matcher.git)
cd resume-matcher

1.Set Up the Virtual Environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

2.Install Dependencies
pip install fastapi uvicorn python-multipart scikit-learn nltk pdfplumber streamlit requests

3. Start the Application
You will need two terminal windows running simultaneously.

Terminal 1: Start the Backend (FastAPI)

python -m uvicorn api:app --reload
The API will be hosted at http://127.0.0.1:8000/docs

Terminal 2: Start the Frontend (Streamlit)

python -m streamlit run app.py
The web app will automatically open in your browser at http://localhost:8501

📁 Project Structure

resume-matcher/
├── api.py           # FastAPI backend server
├── matcher.py       # Core NLP & Machine Learning logic
├── app.py           # Streamlit web frontend
├── .gitignore       # Git ignore rules
└── README.md        # Project documentation