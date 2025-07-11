import streamlit as st
import numpy as np
import joblib

# Load trained model
with open("E:/Machine Learning Projects/heart_disease_model.pkl", "rb") as file:
    model = joblib.load(file)

# Page Configuration
st.set_page_config(page_title="❤️ Heart Disease Predictor", layout="wide")

# Title & Description
st.markdown("""
    <h1 style='text-align: center; color: #d63384;'>❤️ HEART DISEASE PREDICTION APP</h1>
    <p style='text-align: center; font-size:18px;'>Fill the patient information in the sidebar to check the risk of heart disease.</p>
    <hr>
""", unsafe_allow_html=True)

# Sidebar Input Form
st.sidebar.title("📝 PATIENT INFORMATION")

age = st.sidebar.number_input("🧓 AGE", min_value=1, max_value=120, value=40)
sex = st.sidebar.radio("🚻 SEX", ("MALE", "FEMALE"))
cp = st.sidebar.selectbox("💓 CHEST PAIN TYPE", ["TYPICAL ANGINA (0)", "ATYPICAL ANGINA (1)", "NON-ANGINAL PAIN (2)", "ASYMPTOMATIC (3)"])
trestbps = st.sidebar.number_input("🩺 RESTING BLOOD PRESSURE (MM HG)", value=120)
chol = st.sidebar.number_input("🧪 SERUM CHOLESTEROL (MG/DL)", value=200)
fbs = st.sidebar.selectbox("🩸 FASTING BLOOD SUGAR > 120 MG/DL", ["NO (0)", "YES (1)"])
restecg = st.sidebar.selectbox("📈 RESTING ECG RESULT", ["NORMAL (0)", "ST-T ABNORMALITY (1)", "LEFT VENTRICULAR HYPERTROPHY (2)"])
thalach = st.sidebar.number_input("🏃‍♂️ MAXIMUM HEART RATE ACHIEVED", value=150)
exang = st.sidebar.selectbox("😣 EXERCISE INDUCED ANGINA", ["NO (0)", "YES (1)"])
oldpeak = st.sidebar.number_input("📉 OLDPEAK (ST DEPRESSION)", format="%.1f", value=1.0)
slope = st.sidebar.selectbox("📊 SLOPE OF ST SEGMENT", ["UPSLOPING (0)", "FLAT (1)", "DOWNSLOPING (2)"])
ca = st.sidebar.selectbox("🔬 NUMBER OF MAJOR VESSELS COLORED (0–3)", [0, 1, 2, 3])
thal = st.sidebar.selectbox("🧬 THALASSEMIA", ["NORMAL (0)", "FIXED DEFECT (1)", "REVERSIBLE DEFECT (2)"])

# Convert inputs to numeric
sex_val = 1 if sex == "MALE" else 0
cp_val = int(cp.split("(")[-1][0])
fbs_val = int(fbs.split("(")[-1][0])
restecg_val = int(restecg.split("(")[-1][0])
exang_val = int(exang.split("(")[-1][0])
slope_val = int(slope.split("(")[-1][0])
thal_val = int(thal.split("(")[-1][0])

# Prediction Section
st.subheader("🔎 Prediction Result")

if st.button("🔍 PREDICT HEART DISEASE"):
    input_data = np.array([[age, sex_val, cp_val, trestbps, chol, fbs_val,
                            restecg_val, thalach, exang_val, oldpeak,
                            slope_val, ca, thal_val]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success("✅ The person is **NOT LIKELY** to have heart disease.")
        st.balloons()
    else:
        st.error("⚠️ The person **MAY HAVE** heart disease. Further medical testing is advised.")
        st.snow()
with st.expander("ℹ️ FEATURE INFORMATION & MEANING", expanded=False):
    st.markdown("""
    **🔢 AGE:** Patient ki age in years (उम्र)  
    **🚻 SEX:** 1 = MALE, 0 = FEMALE  
    **💓 CHEST PAIN TYPE:**  
    &nbsp;&nbsp;&nbsp;&nbsp;0 = Typical angina – Physical activity se pain  
    &nbsp;&nbsp;&nbsp;&nbsp;1 = Atypical angina – Unusual pain  
    &nbsp;&nbsp;&nbsp;&nbsp;2 = Non-anginal – Non-heart pain  
    &nbsp;&nbsp;&nbsp;&nbsp;3 = Asymptomatic – No pain but risk  

    **🩺 RESTING BLOOD PRESSURE:** Aaram ke dauraan BP (mm Hg)  
    **🧪 SERUM CHOLESTEROL:** Blood mein cholesterol level (mg/dl)  
    **🩸 FASTING BLOOD SUGAR:** >120 mg/dl? → 1 = Yes, 0 = No  
    **📈 RESTING ECG:**  
    &nbsp;&nbsp;&nbsp;&nbsp;0 = Normal, 1 = ST-T abnormal, 2 = Left ventricular hypertrophy  

    **🏃‍♂️ MAX HEART RATE:** Exercise ke dauraan max heart rate  
    **😣 EXERCISE ANGINA:** 1 = Yes, 0 = No  
    **📉 OLDPEAK:** ST depression vs rest (ECG graph ka farak)  
    **📊 ST SLOPE:** 0 = Upslope, 1 = Flat, 2 = Downsloping  
    **🔬 COLORED VESSELS (CA):** 0 to 3 vessels X-ray me dikhi  
    **🧬 THALASSEMIA:**  
    &nbsp;&nbsp;&nbsp;&nbsp;0 = Normal, 1 = Fixed defect, 2 = Reversible defect  
    """)

# Footer
st.markdown("<hr><center>🧠 Built with Streamlit | 🩺 Powered by Machine Learning(Vishal)</center>", unsafe_allow_html=True)
