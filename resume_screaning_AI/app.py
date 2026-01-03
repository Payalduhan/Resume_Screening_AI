import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("resume_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📄 AI Resume Screening System")

resume_text = st.text_area("Paste Resume Text")
job_desc = st.text_area("Paste Job Description")

if st.button("Check Match"):
    combined_text = [resume_text + " " + job_desc]
    vectorized_text = vectorizer.transform(combined_text)
    prediction = model.predict(vectorized_text)

    if prediction[0] == 1:
        st.success("✅ Resume is a GOOD MATCH for this job")
    else:
        st.error("❌ Resume is NOT a good match")