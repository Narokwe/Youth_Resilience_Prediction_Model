# Youth Resilience Prediction Model

This project is a **Machine Learning web application** built with **Streamlit** that predicts the resilience level of youth based on socio-economic, educational, and demographic factors.  
It is designed to support organizations, policymakers, and researchers in identifying youth who may need targeted interventions.

## 📌 Features
- **Interactive Data Input** – Users can enter attributes via a web form.
- **Real-time Prediction** – Get resilience predictions instantly.
- **Data Upload** – Upload a CSV file to run batch predictions.
- **Visualization** – Displays summary statistics and plots for input data.
- **Cloud Deployment** – Easily deployable on Streamlit Cloud.

## 🛠️ Tech Stack
- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- **Streamlit** (Frontend & Deployment)
- **Joblib** (Model saving/loading)

## 📂 Project Structure
.
├── app.py # Main Streamlit application
├── model.pkl # Trained machine learning model
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── youth_resilience.ipynb




## 🚀 Installation & Usage
1. **Clone the repository**
```bash
git clone https://github.com/Narokwe/Youth_Resilience_Prediction_Model.git
cd Youth_Resilience_Prediction_Model
Create a virtual environment & activate it


python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
Install dependencies


pip install -r requirements.txt
Run the app


streamlit run app.py
View in browser
Go to: http://localhost:8501

🌐 Deployment
Deploy to Streamlit Cloud by connecting this repo.

Ensure requirements.txt includes all necessary dependencies.

📊 Model Training
The model was trained on youth resilience datasets using supervised learning techniques (Logistic Regression / Random Forest).
Feature engineering and preprocessing steps included:

Handling missing values

Encoding categorical variables

Scaling numerical features

🤝 Contributing
Contributions are welcome!

Fork the repo

Create your branch (git checkout -b feature-branch)

Commit changes (git commit -m 'Add new feature')

Push to branch (git push origin feature-branch)
