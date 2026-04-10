import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from datetime import datetime
from region_optimizer import (
    get_region_data, get_regional_crop_scores, 
    get_regional_optimal_conditions, get_regional_tips,
    get_seasonal_crops, get_crop_info, 
    adjust_recommendation_for_region, REGION_LIST
)

# Set page config - Mobile-first responsive design
st.set_page_config(
    page_title="🌾 Crop Advisor",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Mobile-Friendly Custom CSS
st.markdown("""
    <style>
    /* Mobile Responsive Design */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Main container */
    .main {
        max-width: 500px;
        margin: 0 auto;
        padding: 10px;
    }
    
    /* Header styling */
    .mobile-header {
        background: linear-gradient(135deg, #2e7d32 0%, #558b2f 100%);
        color: white;
        padding: 20px 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .mobile-header h1 {
        font-size: 28px;
        margin: 10px 0 5px 0;
    }
    
    .mobile-header p {
        font-size: 13px;
        opacity: 0.9;
    }
    
    /* Card styling for better mobile readability */
    .metric-card {
        background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);
        padding: 12px;
        border-radius: 10px;
        margin: 8px 0;
        border-left: 4px solid #2e7d32;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .metric-card-label {
        font-size: 12px;
        color: #666;
        margin-bottom: 4px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .metric-card-value {
        font-size: 22px;
        font-weight: bold;
        color: #2e7d32;
    }
    
    /* Input styling */
    .stNumberInput, .stSlider, .stTextInput {
        margin-bottom: 10px !important;
    }
    
    .stNumberInput label, .stSlider label, .stTextInput label {
        font-size: 13px !important;
        font-weight: 600 !important;
        color: #333 !important;
    }
    
    /* Button styling - Touch-friendly */
    .stButton > button {
        width: 100%;
        padding: 12px 20px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        border: none !important;
        margin-top: 10px !important;
        margin-bottom: 10px !important;
        transition: all 0.3s ease;
        min-height: 50px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Success/Error messages */
    .stSuccess, .stInfo, .stWarning, .stError {
        font-size: 14px;
        padding: 12px !important;
        border-radius: 8px !important;
        margin: 10px 0 !important;
    }
    
    /* Recommendation box */
    .recommendation-box {
        background: linear-gradient(135deg, #c8e6c9 0%, #a5d6a7 100%);
        color: #1b5e20;
        padding: 16px;
        border-radius: 10px;
        text-align: center;
        margin: 15px 0;
        border: 2px solid #2e7d32;
        box-shadow: 0 4px 8px rgba(46, 125, 50, 0.2);
    }
    
    .recommendation-crop {
        font-size: 24px;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .recommendation-confidence {
        font-size: 16px;
        opacity: 0.9;
    }
    
    /* Quick info boxes */
    .info-box {
        background: #f1f8e9;
        border-left: 4px solid #558b2f;
        padding: 10px 12px;
        border-radius: 6px;
        margin: 8px 0;
        font-size: 13px;
    }
    
    /* Section divider */
    .section-divider {
        border: none;
        border-top: 2px solid #b7e1b7;
        margin: 15px 0;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px !important;
        min-height: 45px !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: #f5f5f5;
        border-radius: 8px;
        padding: 10px !important;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 15px;
        font-size: 12px;
        color: #999;
        margin-top: 20px;
        border-top: 1px solid #eee;
    }
    
    /* Responsive text */
    @media (max-width: 480px) {
        .mobile-header h1 {
            font-size: 24px;
        }
        
        .recommendation-crop {
            font-size: 22px;
        }
        
        .stButton > button {
            font-size: 15px !important;
            padding: 12px 16px !important;
            min-height: 48px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Mobile Header
st.markdown("""
    <div class="mobile-header">
        <h1>🌾 Crop Advisor</h1>
        <p>Region-optimized crop recommendations for farmers</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize session state for region
if "selected_region" not in st.session_state:
    st.session_state.selected_region = REGION_LIST[0]

# Region selector in expander (compact design)
with st.expander("📍 **Select Your Region**", expanded=True):
    st.session_state.selected_region = st.selectbox(
        "Choose your farming region:",
        REGION_LIST,
        index=REGION_LIST.index(st.session_state.selected_region),
        key="region_select"
    )
    
    # Display region info
    region_data = get_region_data(st.session_state.selected_region)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-card-label">Climate</div>
                <div class="metric-card-value" style="font-size: 16px;">{region_data.get('climate', 'N/A')}</div>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-card-label">Rainfall</div>
                <div class="metric-card-value" style="font-size: 16px;">{region_data.get('rainfall', 'N/A')}</div>
            </div>
            """, unsafe_allow_html=True)

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

# Create 4-tab mobile-friendly structure
tab1, tab2, tab3, tab4 = st.tabs(["⚡ Quick Input", "🌍 Weather", "📤 Bulk", "📍 Region Info"])

# ========================
# TAB 1: QUICK INPUT
# ========================
with tab1:
    st.subheader("📝 Enter Soil & Climate Data")
    
    # Quick preset buttons for common crops
    st.write("**Quick Presets:**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🌾 Rice", use_container_width=True, key="preset_rice"):
            st.session_state.preset = 'rice'
    with col2:
        if st.button("🌽 Maize", use_container_width=True, key="preset_maize"):
            st.session_state.preset = 'maize'
    with col3:
        if st.button("🥔 Potato", use_container_width=True, key="preset_potato"):
            st.session_state.preset = 'potato'
    
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    
    # Input fields with better mobile spacing
    st.write("**Soil Nutrients (mg/kg):**")
    col1, col2 = st.columns(2)
    
    with col1:
        nitrogen = st.number_input(
            "Nitrogen (N)", 
            min_value=0.0, 
            max_value=200.0, 
            value=50.0,
            step=5.0,
            key="manual_n"
        )
    with col2:
        phosphorus = st.number_input(
            "Phosphorus (P)", 
            min_value=0.0, 
            max_value=150.0, 
            value=50.0,
            step=5.0,
            key="manual_p"
        )
    
    potassium = st.number_input(
        "Potassium (K)", 
        min_value=0.0, 
        max_value=200.0, 
        value=50.0,
        step=5.0,
        key="manual_k"
    )
    
    st.write("**Climate Conditions:**")
    col1, col2 = st.columns(2)
    
    with col1:
        temperature = st.slider(
            "Temperature (°C)", 
            min_value=0.0, 
            max_value=50.0, 
            value=25.0,
            step=0.5,
            key="manual_temp"
        )
    with col2:
        humidity = st.slider(
            "Humidity (%)", 
            min_value=0.0, 
            max_value=100.0, 
            value=60.0,
            step=5.0,
            key="manual_hum"
        )
    
    col1, col2 = st.columns(2)
    with col1:
        ph_value = st.slider(
            "Soil pH", 
            min_value=4.0, 
            max_value=9.0, 
            value=6.5,
            step=0.1,
            key="manual_ph"
        )
    with col2:
        rainfall = st.number_input(
            "Rainfall (mm)", 
            min_value=0.0, 
            max_value=500.0, 
            value=100.0,
            step=10.0,
            key="manual_rain"
        )
    
    # Predict button
    if st.button("🔍 Get Crop Recommendation", key="manual_predict", use_container_width=True):
        with st.spinner("Analyzing your farm data..."):
            try:
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
                base_confidence = model.predict_proba(input_scaled).max() * 100
                
                # Apply regional optimization
                adjusted_confidence, region_factor, region_tips = adjust_recommendation_for_region(
                    base_confidence / 100,
                    crop_name,
                    st.session_state.selected_region,
                    input_data
                )
                adjusted_confidence = adjusted_confidence * 100
                
                # Determine recommendation strength based on region adjustment
                if region_factor > 0.85:
                    recommendation_text = "✅ Highly Recommended for your region"
                elif region_factor > 0.70:
                    recommendation_text = "✓ Good choice for your region"
                else:
                    recommendation_text = "⚠️ Suitable but monitor closely"
                
                # Display recommendation in a prominent box
                st.markdown(f"""
                    <div class="recommendation-box">
                        <div style="font-size: 16px;">🌍 Region-Optimized Recommendation</div>
                        <div class="recommendation-crop">{crop_name.upper()}</div>
                        <div style="font-size: 14px; margin: 8px 0 4px 0;">{recommendation_text}</div>
                        <div class="recommendation-confidence">Overall Confidence: {adjusted_confidence:.1f}%</div>
                        <div style="font-size: 11px; opacity: 0.8;">Base: {base_confidence:.0f}% | Regional Factor: {region_factor*100:.0f}%</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Display input summary with regional comparison
                st.markdown("**📊 Your Farm Data vs Regional Optimal:**")
                optimal_conditions = get_regional_optimal_conditions(st.session_state.selected_region)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("""<div style="font-size: 12px; color: #666; margin-bottom: 8px; text-align: center; text-transform: uppercase;">Your Input</div>""", unsafe_allow_html=True)
                    st.markdown(f"""
                        <div class="metric-card">
                            <div class="metric-card-label">Nitrogen</div>
                            <div class="metric-card-value">{nitrogen}</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-card-label">Temperature</div>
                            <div class="metric-card-value">{temperature}°C</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-card-label">pH Value</div>
                            <div class="metric-card-value">{ph_value}</div>
                        </div>
                        """, unsafe_allow_html=True)
                with col2:
                    st.markdown("""<div style="font-size: 12px; color: #666; margin-bottom: 8px; text-align: center; text-transform: uppercase;">Regional Target</div>""", unsafe_allow_html=True)
                    st.markdown(f"""
                        <div class="metric-card">
                            <div class="metric-card-label">Nitrogen</div>
                            <div class="metric-card-value">{optimal_conditions['nitrogen']}</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-card-label">Temperature</div>
                            <div class="metric-card-value">{region_data.get('avg_temperature', 'N/A')}</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-card-label">pH Value</div>
                            <div class="metric-card-value">{optimal_conditions['ph']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Show regional tips
                if region_tips:
                    st.markdown("**💡 Regional Farming Tips:**")
                    for tip in region_tips:
                        st.markdown(f"- {tip}")
                        
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ========================
# TAB 2: WEATHER-BASED
# ========================
with tab2:
    st.subheader("🌐 Weather-Based Recommendation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        city = st.text_input("City Name", value="Thiruvananthapuram", key="city")
    
    with col2:
        api_key = st.text_input("API Key", type="password", value="6ba29dc3cec671f8c2fd41b3aeb630a4", key="api_key")
    
    st.write("**Soil Nutrients:**")
    col1, col2 = st.columns(2)
    with col1:
        nitrogen_api = st.number_input("Nitrogen", min_value=0.0, value=90.0, step=5.0, key="api_n")
    with col2:
        phosphorus_api = st.number_input("Phosphorus", min_value=0.0, value=42.0, step=5.0, key="api_p")
    
    col1, col2 = st.columns(2)
    with col1:
        potassium_api = st.number_input("Potassium", min_value=0.0, value=43.0, step=5.0, key="api_k")
    with col2:
        ph_api = st.number_input("Soil pH", min_value=4.0, max_value=9.0, value=6.5, key="api_ph")
    
    if st.button("🌍 Get Weather & Recommend", key="api_predict", use_container_width=True):
        with st.spinner(f"Fetching weather for {city}..."):
            try:
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
                response = requests.get(url, timeout=5)
                
                if response.status_code == 200:
                    data = response.json()
                    temperature = data['main']['temp']
                    humidity = data['main']['humidity']
                    rainfall = data.get('rain', {}).get('1h', 0)
                    
                    st.success(f"✅ Weather data loaded for **{city}**")
                    
                    # Display weather
                    st.markdown(f"""
                        <div class="metric-card">
                            <div class="metric-card-label">🌡️ Temperature</div>
                            <div class="metric-card-value">{temperature}°C</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-card-label">💧 Humidity</div>
                            <div class="metric-card-value">{humidity}%</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-card-label">🌧️ Rainfall</div>
                            <div class="metric-card-value">{rainfall} mm</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
                    
                    # Make prediction
                    input_data = {
                        'N': nitrogen_api,
                        'P': phosphorus_api,
                        'K': potassium_api,
                        'temperature': temperature,
                        'humidity': humidity,
                        'ph': ph_api,
                        'rainfall': rainfall
                    }
                    
                    input_df = pd.DataFrame([input_data])
                    input_scaled = scaler.transform(input_df)
                    prediction = model.predict(input_scaled)
                    crop_name = label_encoder.inverse_transform(prediction)[0]
                    base_confidence = model.predict_proba(input_scaled).max() * 100
                    
                    # Apply regional optimization
                    adjusted_confidence, region_factor, region_tips = adjust_recommendation_for_region(
                        base_confidence / 100,
                        crop_name,
                        st.session_state.selected_region,
                        input_data
                    )
                    adjusted_confidence = adjusted_confidence * 100
                    
                    if region_factor > 0.85:
                        recommendation_text = "✅ Highly Recommended for your region"
                    elif region_factor > 0.70:
                        recommendation_text = "✓ Good choice for your region"
                    else:
                        recommendation_text = "⚠️ Suitable but monitor closely"
                    
                    st.markdown(f"""
                        <div class="recommendation-box">
                            <div>🌍 {city}'s Weather + Region</div>
                            <div class="recommendation-crop">{crop_name.upper()}</div>
                            <div style="font-size: 14px; margin: 8px 0 4px 0;">{recommendation_text}</div>
                            <div class="recommendation-confidence">Confidence: {adjusted_confidence:.1f}%</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                else:
                    st.error(f"❌ Could not find city: {city}. Check the spelling and try again.")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ========================
# TAB 3: BULK UPLOAD
# ========================
with tab3:
    st.subheader("📤 Bulk Predictions")
    st.write("Upload a CSV file with columns: N, P, K, temperature, humidity, ph, rainfall")
    
    uploaded_file = st.file_uploader("Choose CSV file", type="csv", key="csv_file")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"✅ Loaded {len(df)} records")
            
            with st.expander("👁️ Preview Data", expanded=False):
                st.dataframe(df.head())
            
            if st.button("🔍 Predict All", key="csv_predict", use_container_width=True):
                with st.spinner("Making predictions with regional optimization..."):
                    required_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
                    if all(col in df.columns for col in required_cols):
                        
                        input_scaled = scaler.transform(df[required_cols])
                        predictions = model.predict(input_scaled)
                        base_confidences = model.predict_proba(input_scaled).max(axis=1) * 100
                        
                        df['Predicted_Crop'] = label_encoder.inverse_transform(predictions)
                        df['Base_Confidence_%'] = base_confidences.round(2)
                        
                        # Apply regional optimization for each row
                        adjusted_confidences = []
                        region_factors = []
                        
                        for idx, row in df.iterrows():
                            input_data = row[required_cols].to_dict()
                            crop = df.loc[idx, 'Predicted_Crop']
                            
                            adj_conf, region_factor, _ = adjust_recommendation_for_region(
                                base_confidences[idx] / 100,
                                crop,
                                st.session_state.selected_region,
                                input_data
                            )
                            adjusted_confidences.append(adj_conf * 100)
                            region_factors.append(region_factor)
                        
                        df['Regional_Confidence_%'] = pd.Series(adjusted_confidences).round(2)
                        df['Region_Factor'] = pd.Series(region_factors).round(2)
                        
                        st.success(f"✅ Predictions Complete! ({len(df)} records processed)")
                        
                        with st.expander("📊 View Results", expanded=True):
                            st.dataframe(df[['Predicted_Crop', 'Base_Confidence_%', 'Regional_Confidence_%', 'Region_Factor']])
                        
                        # Download button
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Results (with regional optimization)",
                            data=csv,
                            file_name="crop_predictions_regional.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                        
                        # Show summary stats
                        st.markdown("**📈 Regional Optimization Summary:**")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            avg_base = df['Base_Confidence_%'].mean()
                            st.metric("Avg Base Confidence", f"{avg_base:.1f}%")
                        with col2:
                            avg_regional = df['Regional_Confidence_%'].mean()
                            st.metric("Avg Regional Confidence", f"{avg_regional:.1f}%")
                        with col3:
                            avg_factor = df['Region_Factor'].mean()
                            st.metric("Avg Region Factor", f"{avg_factor:.2f}")
                    else:
                        st.error(f"❌ Missing required columns: {', '.join(required_cols)}")
                        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# ========================
# TAB 4: REGION INFORMATION
# ========================
with tab4:
    st.subheader("📍 Region-Specific Information")
    
    region_data = get_region_data(st.session_state.selected_region)
    
    # Region overview
    st.markdown(f"### {st.session_state.selected_region}")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-card-label">Climate</div>
                <div style="font-size: 16px; font-weight: bold; color: #2e7d32;">{region_data.get('climate', 'N/A')}</div>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-card-label">Rainfall</div>
                <div style="font-size: 14px; font-weight: bold; color: #2e7d32;">{region_data.get('rainfall', 'N/A')}</div>
            </div>
            """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-card-label">Temperature</div>
                <div style="font-size: 14px; font-weight: bold; color: #2e7d32;">{region_data.get('avg_temperature', 'N/A')}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    
    # Suitable crops
    st.markdown("**🌾 Crops Suitable for This Region:**")
    crop_scores = get_regional_crop_scores(st.session_state.selected_region)
    if crop_scores:
        # Sort by suitability score
        sorted_crops = sorted(crop_scores.items(), key=lambda x: x[1], reverse=True)
        
        cols = st.columns(2)
        for idx, (crop, score) in enumerate(sorted_crops):
            with cols[idx % 2]:
                crop_info = get_crop_info(crop)
                crop_icon = crop_info.get('icon', '🌾')
                
                # Color code based on suitability
                if score >= 85:
                    color = "#4caf50"  # Green
                    rating = "⭐⭐⭐"
                elif score >= 70:
                    color = "#ffc107"  # Amber
                    rating = "⭐⭐"
                else:
                    color = "#ff9800"  # Orange
                    rating = "⭐"
                
                st.markdown(f"""
                    <div class="metric-card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <div class="metric-card-label">{crop_icon} {crop}</div>
                                <div style="color: {color}; font-weight: bold; font-size: 14px;">{rating}</div>
                            </div>
                            <div style="font-size: 20px; color: {color};">{score}%</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    
    # Seasonal crops
    st.markdown("**📅 Seasonal Crops:**")
    seasonal_data = get_seasonal_crops(st.session_state.selected_region)
    if seasonal_data:
        for season, crops in seasonal_data.items():
            st.markdown(f"**{season}:**")
            st.markdown(", ".join([f"{crop}" for crop in crops]))
    
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    
    # Optimal soil conditions
    st.markdown("**🌱 Optimal Soil Conditions:**")
    optimal = get_regional_optimal_conditions(st.session_state.selected_region)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-card-label">N (mg/kg)</div>
                <div class="metric-card-value" style="font-size: 18px;">{optimal['nitrogen']}</div>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-card-label">P (mg/kg)</div>
                <div class="metric-card-value" style="font-size: 18px;">{optimal['phosphorus']}</div>
            </div>
            """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-card-label">K (mg/kg)</div>
                <div class="metric-card-value" style="font-size: 18px;">{optimal['potassium']}</div>
            </div>
            """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-card-label">pH</div>
                <div class="metric-card-value" style="font-size: 18px;">{optimal['ph']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    
    # Farming tips
    st.markdown("**💡 Regional Farming Tips:**")
    tips = get_regional_tips(st.session_state.selected_region)
    if tips:
        for tip in tips:
            st.markdown(f"- {tip}")
    
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    
    # States in region
    if 'states' in region_data:
        st.markdown("**📍 States in This Region:**")
        st.markdown(", ".join(region_data['states']))

# ========================
# FOOTER
# ========================
st.markdown("""
    <div class="footer">
        <p><strong>🌾 Crop Advisor</strong> | Region-Optimized AI Recommendations</p>
        <p>🤖 Model: Random Forest | 📊 Features: 7 | 🌍 Regions: 6</p>
        <p style="font-size: 11px; margin-top: 8px;">⚠️ For guidance only. Always consult local agricultural experts.</p>
    </div>
    """, unsafe_allow_html=True)
