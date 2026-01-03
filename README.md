Resume Screening AI

🚀 An AI-powered system that automatically screens resumes using NLP & Machine Learning.

 🔍 Overview
This project analyzes resume text and predicts whether a candidate is suitable for a job role.

 🛠️ Tech Stack
- 🐍 Python  
- 📊 Pandas, NumPy  
- 🤖 Scikit-learn  
- 🧠 NLP (TF-IDF)  
- 🌐 Streamlit  

 ⚙️ How It Works
➡️ Resume Text Input  
➡️ Text Preprocessing  
➡️ TF-IDF Feature Extraction  
➡️ Logistic Regression Classification  

 📁 Project Structure
│
├── app.py                # Streamlit web application
├── model.py              # Model training & saving logic
├── resumemodel.pkl       # Trained Logistic Regression model
├── vectorizer.pkl        # TF-IDF vectorizer
├── resumes.csv           # Resume dataset (text + label)
└── README.md             # Project documentation 

▶️ How to Run
▶️ pip install -r requirements.txt  
▶️ python model.py  
▶️ streamlit run app.py  

 🎯 Output
✅ Suitable  
❌ Not Suitable

