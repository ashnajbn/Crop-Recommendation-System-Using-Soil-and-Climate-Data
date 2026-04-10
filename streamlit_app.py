import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
    }
    .header {
        text-align: center;
        color: #2e7d32;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.markdown("<h1 class='header'>🌾 Crop Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("---")
st.write("Get personalized crop recommendations based on soil and climate data.")

# Load models
@st.cache_resource
def load_models():
    try:
        model = joblib.load('model.pkl')
        scaler = joblib.load('scaler.pkl')
        label_encoder = joblib.load('label_encoder.pkl')
        return model, scaler, label_encoder
    except FileNotFoundError:
        st.error("❌ Models not found! Please train and save the models first.")
        return None, None, None

model, scaler, label_encoder = load_models()

if model is None:
    st.stop()

# Sidebar for input method selection
st.sidebar.header("Input Method")
input_method = st.sidebar.radio("Choose input method:", 
                                ["Manual Input", "Weather API", "Upload CSV"])

# ========================
# MANUAL INPUT TAB
# ========================
if input_method == "Manual Input":
    st.sidebar.header("📊 Soil & Climate Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nitrogen = st.number_input(
            "Nitrogen (N) (mg/kg)", 
            min_value=0.0, 
            max_value=200.0, 
            value=50.0,
            help="Amount of nitrogen in soil"
        )
        phosphorus = st.number_input(
            "Phosphorus (P) (mg/kg)", 
            min_value=0.0, 
            max_value=150.0, 
            value=50.0,
            help="Amount of phosphorus in soil"
        )
        potassium = st.number_input(
            "Potassium (K) (mg/kg)", 
            min_value=0.0, 
            max_value=200.0, 
            value=50.0,
            help="Amount of potassium in soil"
        )
        temperature = st.slider(
            "Temperature (°C)", 
            min_value=0.0, 
            max_value=50.0, 
            value=25.0,
            step=0.1
        )
    
    with col2:
        humidity = st.slider(
            "Humidity (%)", 
            min_value=0.0, 
            max_value=100.0, 
            value=60.0,
            step=1.0
        )
        ph_value = st.slider(
            "Soil pH", 
            min_value=4.0, 
            max_value=9.0, 
            value=6.5,
            step=0.1
        )
        rainfall = st.number_input(
            "Rainfall (mm)", 
            min_value=0.0, 
            max_value=500.0, 
            value=100.0,
            help="Expected annual rainfall"
        )
    
    # Create input dataframe
    input_data = {
        'N': nitrogen,
        'P': phosphorus,
        'K': potassium,
        'temperature': temperature,
        'humidity': humidity,
        'ph': ph_value,
        'rainfall': rainfall
    }
    
    # Predict
    if st.button("🔍 Get Recommendation", key="manual_predict"):
        with st.spinner("Analyzing soil and climate data..."):
            try:
                input_df = pd.DataFrame([input_data])
                input_scaled = scaler.transform(input_df)
                prediction = model.predict(input_scaled)
                crop_name = label_encoder.inverse_transform(prediction)[0]
                confidence = model.predict_proba(input_scaled).max() * 100
                
                st.success(f"✅ Recommended Crop: **{crop_name}**")
                st.metric("Confidence", f"{confidence:.2f}%")
                
                # Display input summary
                st.subheader("📋 Input Summary")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Nitrogen", f"{nitrogen} mg/kg")
                    st.metric("Temperature", f"{temperature}°C")
                with col2:
                    st.metric("Phosphorus", f"{phosphorus} mg/kg")
                    st.metric("Humidity", f"{humidity}%")
                with col3:
                    st.metric("Potassium", f"{potassium} mg/kg")
                    st.metric("pH", f"{ph_value}")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ========================
# WEATHER API TAB
# ========================
elif input_method == "Weather API":
    st.subheader("🌐 Weather-Based Recommendation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        city = st.text_input("Enter City Name", value="Thiruvananthapuram", 
                            help="Get weather data from OpenWeatherMap API")
        api_key = st.text_input("API Key (from openweathermap.org)", 
                               type="password",
                               value="6ba29dc3cec671f8c2fd41b3aeb630a4")
    
    with col2:
        nitrogen = st.number_input("Nitrogen (N) (mg/kg)", min_value=0.0, value=90.0, key="api_n")
        phosphorus = st.number_input("Phosphorus (P) (mg/kg)", min_value=0.0, value=42.0, key="api_p")
        potassium = st.number_input("Potassium (K) (mg/kg)", min_value=0.0, value=43.0, key="api_k")
        ph_value = st.number_input("Soil pH", min_value=4.0, max_value=9.0, value=6.5, key="api_ph")
    
    if st.button("🌍 Fetch Weather & Predict", key="api_predict"):
        with st.spinner(f"Fetching weather data for {city}..."):
            try:
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
                response = requests.get(url, timeout=5)
                
                if response.status_code == 200:
                    data = response.json()
                    temperature = data['main']['temp']
                    humidity = data['main']['humidity']
                    rainfall = data.get('rain', {}).get('1h', 0)
                    
                    st.success(f"✅ Weather Data Retrieved for {city}")
                    
                    # Display weather
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("🌡️ Temperature", f"{temperature}°C")
                    with col2:
                        st.metric("💧 Humidity", f"{humidity}%")
                    with col3:
                        st.metric("🌧️ Rainfall", f"{rainfall} mm")
                    
                    # Make prediction
                    input_data = {
                        'N': nitrogen,
                        'P': phosphorus,
                        'K': potassium,
                        'temperature': temperature,
                        'humidity': humidity,
                        'ph': ph_value,
                        'rainfall': rainfall
                    }
                    
                    input_df = pd.DataFrame([input_data])
                    input_scaled = scaler.transform(input_df)
                    prediction = model.predict(input_scaled)
                    crop_name = label_encoder.inverse_transform(prediction)[0]
                    confidence = model.predict_proba(input_scaled).max() * 100
                    
                    st.success(f"✅ Recommended Crop: **{crop_name}**")
                    st.metric("Confidence", f"{confidence:.2f}%")
                    
                else:
                    st.error(f"❌ Error: Could not fetch weather data. Check city name and API key.")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ========================
# BULK PREDICTION TAB
# ========================
elif input_method == "Upload CSV":
    st.subheader("📤 Bulk Predictions from CSV")
    st.write("Upload a CSV file with columns: N, P, K, temperature, humidity, ph, rainfall")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write(f"✅ Loaded {len(df)} records")
            st.dataframe(df.head())
            
            if st.button("🔍 Predict All Crops", key="csv_predict"):
                with st.spinner("Making predictions..."):
                    # Check required columns
                    required_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
                    if all(col in df.columns for col in required_cols):
                        
                        # Scale and predict
                        input_scaled = scaler.transform(df[required_cols])
                        predictions = model.predict(input_scaled)
                        confidences = model.predict_proba(input_scaled).max(axis=1) * 100
                        
                        # Add results
                        df['Predicted_Crop'] = label_encoder.inverse_transform(predictions)
                        df['Confidence_%'] = confidences.round(2)
                        
                        st.success("✅ Predictions Complete!")
                        st.dataframe(df[required_cols + ['Predicted_Crop', 'Confidence_%']])
                        
                        # Download results
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Results",
                            data=csv,
                            file_name="crop_predictions.csv",
                            mime="text/csv"
                        )
                    else:
                        st.error(f"❌ CSV must contain columns: {', '.join(required_cols)}")
                        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# ========================
# FOOTER
# ========================
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📚 **Model**: Random Forest Classifier")

with col2:
    st.info("📊 **Features**: 7 (N, P, K, Temp, Humidity, pH, Rainfall)")

with col3:
    st.info(f"⏰ **Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.markdown("""
---
<div style="text-align: center;">
    <p>🌾 <strong>Crop Recommendation System</strong> | Made with Streamlit 🚀</p>
    <p style="font-size: 12px; color: gray;">For agricultural predictions only. Always consult local experts.</p>
</div>
""", unsafe_allow_html=True)
