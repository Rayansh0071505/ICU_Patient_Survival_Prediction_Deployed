import pickle
import pandas as pd
import numpy as np
import streamlit as st

# Load the model
model = pickle.load(open("model.pkl","rb"))

# Defome a function to make prediction
def predict_cancellation(features):
    prediction = model.predict(features)
    return prediction

def main():
    st.title("ICU Patient Survival Prediction")
    st.write("This app predict whether the patient will survive or not")

    # Collect user input for prediction
    alp = st.text_input("ALP (Alkaline Phosphatase)")
    st.write("An enzyme produced mainly by the liver and bones. Elevated levels may indicate liver or bone disorders.")

    alt = st.text_input("ALT (Alanine Aminotransferase)")
    st.write("An enzyme that can signal liver damage or disease, often associated with conditions like hepatitis.")

    ast = st.text_input("AST (Aspartate Aminotransferase)")
    st.write(" An enzyme found in various body tissues, particularly the liver and heart. Elevated levels can indicate liver or heart issues.")

    age = st.text_input("Age")

    bun = st.text_input("BUN (Blood Urea Nitrogen)")
    st.write("A measure of kidney function and hydration levels. Elevated levels may indicate kidney problems or dehydration.")

    Bilirubin = st.text_input("Bilirubin")
    st.write("A yellowish substance created during the normal breakdown of red blood cells. Elevated levels can indicate liver or blood disorders.")

    creatinine = st.text_input("Creatinine")
    st.write("A waste product from muscle metabolism that's filtered out by the kidneys. Elevated levels can suggest kidney dysfunction.")

    glucose = st.text_input("Glucose")
    st.write("Blood sugar level. Monitoring glucose is crucial, especially for diabetic patients or those at risk of developing diabetes.")

    hr = st.text_input("Heart Rate")

    k = st.text_input("Potassium level")
    st.write("An essential electrolyte critical for nerve and muscle cell functioning. Abnormal levels can affect heart rhythm.")

    lactate = st.text_input("Lactate")
    st.write("Elevated levels may indicate tissue hypoxia (low oxygen levels) and can be a sign of severe infections or sepsis.")

    mg = st.text_input("Magnesium level")
    st.write("An electrolyte important for nerve and muscle function, as well as heart rhythm. Abnormal levels can be harmful.")

    na = st.text_input("Sodium level")
    st.write("An electrolyte critical for fluid balance and nerve function. Abnormal levels can indicate various health issues")

    resprate = st.text_input("Respiratory Rate")
    st.write("he number of breaths per minute. An important vital sign indicating respiratory health and distress.")

    st.write("Proteins indicating heart muscle damage. Elevated levels can suggest a heart attack or other cardiac issues.")
    tnl = st.text_input("TroponinI")
    tnt = st.text_input("TroponinT")

    wbc = st.text_input("White Blood cells")

    pH = st.text_input("pH")
    st.write(" A measure of blood acidity or alkalinity. Imbalances can indicate respiratory or metabolic issues.")

    if st.button("Predict"):

        input_features = np.array([
            alp,
alt,
ast,
age,
bun,
Bilirubin,
creatinine,
glucose,
hr,
k,
lactate,
mg,
na,
resprate,
tnl,
tnt,
wbc,
pH
        ])


        input_features = input_features.flatten()
        input_features = np.array(input_features).reshape(1, -1)
        prediction = predict_cancellation(input_features)

        if prediction == 1:
            st.write("Prediction: Patient is not going to be survived")
        else:
            st.write("Prediction: Patient is going to be survived")

if __name__ == "__main__":
    main()





