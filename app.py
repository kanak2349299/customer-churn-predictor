import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📊", layout="wide")

st.markdown("""
<style>
/* Main Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Sidebar - Glassmorphism */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(102, 126, 234, 0.95) 0%, rgba(118, 75, 162, 0.95) 100%);
    backdrop-filter: blur(10px);
    border-right: 1px solid rgba(255,255,255,0.2);
}
[data-testid="stSidebar"] * {
    color: white!important;
}

/* Make Sidebar Title/Dashboard extra bright */
[data-testid="stSidebar"] h1 {
    color: white!important;
    font-weight: 800;
    text-shadow: 0 0 10px rgba(255,255,255,0.3);
}

/* Main text */
h2, h3, p, label, div {
    color: #E0E0E0!important;
}

/* CENTER WHITE HEADING */
h1 {
    text-align: center;
    color: white!important;
    font-weight: 800;
    text-shadow: 0 0 15px rgba(102, 126, 234, 0.6);
    animation: fadeIn 1.5s ease-in;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-10px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 15px rgba(102, 126, 234, 0.5);
}

/* Risk Boxes */
.risk-box {
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    animation: slideUp 0.8s ease;
}
@keyframes slideUp {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
.low {background: linear-gradient(90deg, #11998e, #38ef7d); color: white;}
.medium {background: linear-gradient(90deg, #f7971e, #ffd200); color: black;}
.high {background: linear-gradient(90deg, #eb3349, #f45c43); color: white;}

/* Metric Cards */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Expander animation */
[data-testid="stExpander"] {
    animation: fadeIn 0.6s ease;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource()
def load_model():
    rf_model = pickle.load(open('customer_churn_model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    return rf_model, scaler

model, scaler = load_model()

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=120)
    st.title("📊Dashboard") 
    st.markdown("<p style='text-align: center;font-size:20px;font-weight: bold; color: white;'>Predict & Retain Customers</p>", unsafe_allow_html=True)
  
    st.divider()

    with st.expander("**ℹ️ About** "):
        st.write("**Customer Churn** means when a customer stops using your service." \
        "This Machine Learning application predicts whether a customer is likely to churn or continue using company's services based on customer demographics,subscription details,and service usage." \
        " Predicting churn helps companies retain customers and save revenue.")

    with st.expander("**🎯Objective**"):
        st.write("""
        - To predict customer churn 
        - Help businesses identify at-risk customers
        - Support customer retention strategies""")

    with st.expander("**💁🏻‍♀️Model Info**"):
        st.write("**Problem Type:** Binary Classification")
        st.write("**Algorithm:** ✅ Random Forest Classifier")
        st.write("**Evaluation Metrics:**") 
        st.markdown("""
        - ✅ Accuracy Score
        - ✅ Confusion Matrix
        - ✅ Classification Report
        - ✅ Precision
        - ✅ Recall
        - ✅ F1-Score
        """)
        st.write("**Accuracy:** ~85%")

    with st.expander("**📂Dataset Info**"):
        st.write("**Dataset:** Telco Customer Churn ")
        st.write("**Target Variable:** Churn (Yes/No)")

    with st.expander("**🛠️Tech Stack**"):
        st.write("**Frontend:** Streamlit")
        st.write("**Backend:** Python")
        st.write("**Libraries:**") 
        st.markdown("""
        - Pandas
        - NumPy
        - Scikit-learn
        - Streamlit
        -  Pickle
        """)

    with st.expander("**👩🏻‍💻 Developer**"):
        st.write("**Himangi Gupta😊**")
        st.write("🔗[GitHub ](https://github.com/kanak2349299)")
    st.markdown(" ")
    st.info('💡Fill in the customer details and click Predict Churn to view the prediction.')
    st.divider()
    st.image("https://cdn-icons-png.flaticon.com/512/6997/6997662.png", width=80) 
    st.caption("Retention is cheaper than Acquisition")

st.title("Customer Churn Prediction System") 
st.write("Fill customer details below to predict churn risk and get retention recommendations")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

with col2:
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

col3, col4 = st.columns(2)
with col3:
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
with col4:
    PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

if st.button("🔮 Predict Churn", use_container_width=True):

    input_data = pd.DataFrame([[gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines,
                               InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
                               StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
                               MonthlyCharges, TotalCharges]],
                             columns=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
                                     'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                                     'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                                     'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'])

    map_yes_no = {'Yes': 1, 'No': 0}
    map_gender = {'Male': 1, 'Female': 0}
    map_internet = {'DSL': 0, 'Fiber optic': 1, 'No': 2}
    map_no_service = {'Yes': 1, 'No': 0, 'No internet service': 2, 'No phone service': 2}

    input_data['gender'] = input_data['gender'].map(map_gender)
    input_data['Partner'] = input_data['Partner'].map(map_yes_no)
    input_data['Dependents'] = input_data['Dependents'].map(map_yes_no)
    input_data['PhoneService'] = input_data['PhoneService'].map(map_yes_no)
    input_data['PaperlessBilling'] = input_data['PaperlessBilling'].map(map_yes_no)
    input_data['InternetService'] = input_data['InternetService'].map(map_internet)
    input_data['OnlineSecurity'] = input_data['OnlineSecurity'].map(map_no_service)
    input_data['OnlineBackup'] = input_data['OnlineBackup'].map(map_no_service)
    input_data['DeviceProtection'] = input_data['DeviceProtection'].map(map_no_service)
    input_data['TechSupport'] = input_data['TechSupport'].map(map_no_service)
    input_data['StreamingTV'] = input_data['StreamingTV'].map(map_no_service)
    input_data['StreamingMovies'] = input_data['StreamingMovies'].map(map_no_service)

    input_data = pd.get_dummies(input_data, columns=['Contract', 'PaymentMethod', 'MultipleLines'], drop_first=True)

    for col in scaler.feature_names_in_:
        if col not in input_data.columns:
            input_data[col] = 0
    input_data = input_data[scaler.feature_names_in_]

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    prob = model.predict_proba(input_scaled)[0][1]
    risk_score = prob * 100

    st.divider()
    st.subheader("📈 Prediction Result")

    col_res1, col_res2 = st.columns([1,1])
    with col_res1:
        st.metric("Churn Risk Score", f"{risk_score:.2f}%")
        st.progress(int(risk_score))

    with col_res2:
        if prediction[0] == 1:
            st.error(f"⚠️ Prediction: CUSTOMER WILL CHURN")
        else:
            st.success(f"✅ Prediction: CUSTOMER WILL STAY")

    st.subheader("💡 Recommendation")
    if risk_score < 30:
        st.markdown('<div class="risk-box low">🟢 LOW RISK <br> Continue providing current services. <br> Send thank you email.</div>', unsafe_allow_html=True)
    elif risk_score < 70:
        st.markdown('<div class="risk-box medium">🟡 MEDIUM RISK <br> Offer a loyalty reward. <br> Check customer satisfaction survey.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="risk-box high">🔴 HIGH RISK <br> Contact the customer immediately. <br> Offer discount or upgraded plan. <br> Assign a support representative.</div>', unsafe_allow_html=True)