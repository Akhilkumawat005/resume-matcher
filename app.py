import streamlit as st
import requests

st.title("AI Resume Matcher")
st.write("Compare a resume against a job description instantly.")

# Input fields
job_desc = st.text_area("Paste the Job Description here:")
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Calculate Match"):
    if job_desc and uploaded_file:
        with st.spinner("Analyzing..."):
            # Package the data to send to FastAPI
            files = {"resume": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
            data = {"job_description": job_desc}

            try:
                # Send request to your FastAPI server
                response = requests.post("http://127.0.0.1:8000/match/", data=data, files=files)
                result = response.json()

                # Display results
                st.success(f"Match Score: **{result['match_percentage']}%**")
            except Exception as e:
                st.error("Could not connect to the server. Is your FastAPI server running?")
    else:
        st.warning("Please provide both a job description and a resume.")