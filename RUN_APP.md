# 🚀 Quick Start Guide - Streamlit Web App

## Step 1: Ensure Models are Trained

First, make sure your models are saved by running the Jupyter notebook:
```python
import joblib

# In your notebook, after training the model, run:
joblib.dump(rf_model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(le, 'label_encoder.pkl')
```

Verify files exist in your project directory:
- ✅ `model.pkl` (trained Random Forest)
- ✅ `scaler.pkl` (feature scaler)
- ✅ `label_encoder.pkl` (crop label encoder)

---

## Step 2: Activate Virtual Environment

**PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

**Command Prompt (cmd):**
```cmd
.venv\Scripts\activate.bat
```

**Expected output:**
```
(.venv) PS C:\Users\sanan\OneDrive\Documents\GitHub\Crop-Recommendation-System-Using-Soil-and-Climate-Data>
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install just Streamlit:
```bash
pip install streamlit
```

---

## Step 4: Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

**Expected output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

---

## Step 5: Access the Web App

The app automatically opens in your default browser at:
- **Local**: `http://localhost:8501`
- **Network**: `http://192.168.x.x:8501` (access from other devices on same network)

---

## 🎯 Using the App

### **Mode 1: Manual Input** 📝
1. Adjust sliders for soil nutrients (N, P, K)
2. Set climate parameters (Temperature, Humidity, pH, Rainfall)
3. Click "Get Recommendation"
4. View predicted crop + confidence score

### **Mode 2: Weather API** 🌍
1. Enter city name (e.g., "New York")
2. Enter OpenWeatherMap API key (get free at openweathermap.org)
3. Input soil parameters
4. Click "Fetch Weather & Predict"
5. App fetches real weather data and predicts

### **Mode 3: Bulk CSV Upload** 📤
1. Prepare CSV with columns: `N, P, K, temperature, humidity, ph, rainfall`
2. Upload file
3. Click "Predict All Crops"
4. Download results CSV with predictions

---

## 🔑 Getting OpenWeatherMap API Key

1. Go to [openweathermap.org](https://openweathermap.org/api)
2. Sign up for free account
3. Go to API keys section
4. Copy your key
5. Paste in Streamlit app

**Default test key works for some cities (Thiruvananthapuram)**

---

## 📊 Sample CSV Format

Create `crops_data.csv`:
```csv
N,P,K,temperature,humidity,ph,rainfall
90,42,43,20,82,6.5,202.9
20,30,40,30,60,7.0,100
50,50,50,25,70,6.8,150
```

Then upload in the app!

---

## ⚙️ Troubleshooting

### **App doesn't start**
```bash
# Check if streamlit is installed
pip list | findstr streamlit

# Reinstall if needed
pip install streamlit --upgrade
```

### **"No module named 'tensorflow'"**
```bash
pip install tensorflow
```

### **"Models not found" error**
```bash
# Run the notebook to train and save models first
# Then verify files exist:
# - model.pkl ✓
# - scaler.pkl ✓
# - label_encoder.pkl ✓
```

### **Port 8501 already in use**
```bash
# Use different port
streamlit run streamlit_app.py --server.port=8502
```

### **API key not working**
- Verify API key is correct at openweathermap.org
- Check internet connection
- Try a different city name

---

## 🌐 Deploy Online

### **Option 1: Streamlit Cloud (Recommended)**
```bash
# 1. Push code to GitHub
git add .
git commit -m "Deploy to Streamlit Cloud"
git push

# 2. Go to share.streamlit.io
# 3. Connect GitHub repo
# 4. Select streamlit_app.py
# 5. Click "Deploy"
```

### **Option 2: Docker**
```bash
# Build image
docker build -t crop-recommender .

# Run container
docker run -p 8501:8501 crop-recommender

# Access at http://localhost:8501
```

### **Option 3: Render.com**
```bash
# Push to GitHub, then:
# 1. Go to render.com
# 2. New > Web Service
# 3. Connect repo
# 4. Set build: pip install -r requirements.txt
# 5. Set start: streamlit run streamlit_app.py --server.port=10000
# 6. Deploy
```

---

## 🎨 Customization

### Change App Title/Icon
Edit `streamlit_app.py`:
```python
st.set_page_config(
    page_title="Your App Title",
    page_icon="🌾",  # Change emoji
)
```

### Change Color Scheme
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#2e7d32"      # Green
backgroundColor = "#ffffff"   # White
secondaryBackgroundColor = "#f0f2f6"  # Light gray
```

### Add More Features
```python
# Add new tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Content for tab 1")
```

---

## 📈 Next Steps

- ✅ Test all 3 prediction modes
- ✅ Deploy to Streamlit Cloud
- ✅ Share with friends/family
- ✅ Add more crops to model
- ✅ Integrate with database for predictions history
- ✅ Add charts and visualizations

---

**Enjoy your Crop Recommendation Web App! 🌾**

For more info: [Streamlit Docs](https://docs.streamlit.io)
