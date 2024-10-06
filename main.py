import streamlit as st
import pickle
import pandas as pd

# Load the model
with open("rf.pkl", "rb") as f:
    model = pickle.load(f)
# Create the Streamlit app
st.title('Diabetes Prediction')

# Create input fields for the features
Pregnancies = st.number_input('Pregnancies', min_value=0)
Glucose = st.number_input('Glucose', min_value=0)
BloodPressure = st.number_input('BloodPressure', min_value=0)
SkinThickness = st.number_input('SkinThickness', min_value=0)
Insulin = st.number_input('Insulin', min_value=0)
BMI = st.number_input('BMI', min_value=0.0)
DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0.0)
Age = st.number_input('Age', min_value=0)

# Create a button to trigger the prediction
if st.button('Predict'):
    # Create a dataframe from the input features
    input_data = pd.DataFrame({
        'Pregnancies': [Pregnancies],
        'Glucose': [Glucose],
        'BloodPressure': [BloodPressure],
        'SkinThickness': [SkinThickness],
        'Insulin': [Insulin],
        'BMI': [BMI],
        'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
        'Age': [Age]
    })

    # Make the prediction
    prediction = model.predict(input_data)

    # Display the prediction
    if prediction[0] == 0:
        st.success('The person is not diabetic')
    else:
        st.error('The person is diabetic')