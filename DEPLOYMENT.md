#  Crop Recommendation System - Deployment Guide

## Running the Streamlit App Locally

### Prerequisites
✅ Python 3.8+ with virtual environment activated
✅ All dependencies installed (`pip install -r requirements.txt`)
✅ Trained models saved as:
   - `model.pkl`
   - `scaler.pkl`
   - `label_encoder.pkl`

### 1️ Activate Virtual Environment
```bash
# PowerShell
.venv\Scripts\Activate.ps1

# Command Prompt
.venv\Scripts\activate.bat
```

### 2️ Run the Streamlit App
```bash
streamlit run streamlit_app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

##  Features

### **Manual Input Mode**
- Input soil parameters (N, P, K)
- Set climate conditions (Temperature, Humidity, pH, Rainfall)
- Get instant crop recommendations with confidence scores

### **Weather API Mode**
- Fetch real-time weather data from OpenWeatherMap
- Automatically input climate data for any city
- Combine with soil parameters for predictions

### **Bulk Prediction Mode**
- Upload CSV with soil/climate data
- Get recommendations for multiple locations
- Download results as CSV

---

##  Deployment Options

### **Option 1: Streamlit Cloud (Easiest)**
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Select `streamlit_app.py` as main file
5. Deploy with one click!

> Note: Add `runtime.txt` to pin Python to `python-3.12.4` so Streamlit Cloud uses a supported Python version.

```
Pros: Free, automatic updates, easy sharing
Cons: Limited resources
```

### **Option 2: Render (Free Tier Available)**
1. Push code to GitHub
2. Create account at [render.com](https://render.com)
3. New > Web Service
4. Connect GitHub repo
5. Set as Python 3.11
6. Commands:
   - Build: `pip install -r requirements.txt`
   - Start: `streamlit run streamlit_app.py --server.port=10000`

### **Option 3: Docker Container**

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t crop-recommender .
docker run -p 8501:8501 crop-recommender
```

### **Option 4: AWS, Google Cloud, Azure**
Deploy Docker container or use Streamlit Cloud integration

---

## 🔧 Configuration

### Streamlit Config (`.streamlit/config.toml`)
```toml
[theme]
primaryColor = "#2e7d32"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[client]
showErrorDetails = false

[server]
maxUploadSize = 10
enableXsrfProtection = true
```

### Environment Variables
Create `.env` file:
```
OPENWEATHER_API_KEY=your_api_key_here
MODEL_PATH=./model.pkl
SCALER_PATH=./scaler.pkl
ENCODER_PATH=./label_encoder.pkl
```

---

##  File Structure
```
Crop-Recommendation-System/
├── streamlit_app.py          # Main web app
├── model.pkl                 # Trained model
├── scaler.pkl                # Feature scaler
├── label_encoder.pkl         # Crop encoder
├── requirements.txt          # Dependencies
├── Dockerfile                # Docker config
├── .streamlit/
│   └── config.toml          # Streamlit config
├── Crop_Recommendation_System.ipynb
└── README.md
```

---

##  Testing

Test the app locally first:
```bash
streamlit run streamlit_app.py
```

Then test all features:
- ✅ Manual input predictions
- ✅ Weather API integration
- ✅ CSV bulk upload
- ✅ Download functionality

---

##  Security Notes

 **API Key Protection**:
- Don't commit API keys to GitHub
- Use environment variables or Streamlit secrets
- Streamlit Cloud Secrets Manager:
  1. Go to your app settings
  2. Add under "Secrets"
  3. Access in app: `st.secrets["api_key"]`

 **Model Protection**:
- Models are in `.pkl` format (pickle)
- Keep them secure on deployed servers
- Consider encryption for production

---

##  Performance Optimization

### Caching (Already Implemented)
```python
@st.cache_resource
def load_models():
    # Models load only once
    ...
```

### Input Validation
- Check CSV columns exist
- Validate parameter ranges
- Error handling for API failures

---

##  Troubleshooting

### **"Models not found" Error**
```bash
# Train and save models in notebook first
python -c "import joblib; print(joblib.load('model.pkl'))"
```

### **API Key Errors**
- Verify API key is valid at openweathermap.org
- Check internet connection
- Use test city: "London"

### **Long Paths Error (Windows)**
Fix with:
```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

### **Streamlit Not Found**
```bash
pip install streamlit==1.28.0
```

---

##  Mobile Access

The Streamlit app is mobile-responsive! Access from:
- Same network: `http://your_ip:8501`
- Remote Server: Use deployed URL

---

##  Support & Next Steps

1. **Enhance UI**: Add charts, model explanations
2. **Add Alerts**: Notify on extreme conditions
3. **Database**: Store predictions for analytics
4. **Multiple Models**: Compare different ML algorithms
5. **Mobile App**: Build with Flutter/React Native

---

**Happy Farming! 🌾**
