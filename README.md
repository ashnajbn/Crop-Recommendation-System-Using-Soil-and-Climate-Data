# Crop Recommendation System 

A Machine Learning based Predictive Analytics Project  

## Crop Recommendation using Machine Learning  

## Project Overview  
This project focuses on building a **Crop Recommendation System** using Machine Learning techniques. The model suggests the most suitable crop to grow based on environmental and soil parameters such as **Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall**.

This system helps farmers and agricultural planners make **data-driven decisions** to improve productivity and optimize crop yield.

---

## Features  
- 🎯 Machine Learning-based crop recommendations
- 📱 **Mobile-optimized responsive interface** for smartphones & tablets
- 🌍 Real-time weather API integration (OpenWeatherMap)
- 📊 Interactive data visualization and analytics
- 📤 Bulk prediction capability (CSV upload)
- 💾 Model caching for fast predictions
- 🔒 Secure, offline-capable predictions
- 📈 Comprehensive accuracy metrics
- 🌾 Farmer-friendly UI with intuitive controls
- 🎡 Tab-based navigation for easy mobile access  

---

##  Project Structure  
```bash
Crop-Recommendation-System/
│
├── Crop Recommendation System.ipynb # Main notebook
├── .gitignore # Ignore dataset & unnecessary files
├── README.md # Project documentation
└── Crop_recommendation.csv/ # Dataset folder (not included in repo)
```

---

## 📊 Dataset  
The dataset contains agricultural and environmental parameters used to recommend crops.

Download it from:https://www.kaggle.com/code/sajjadalishah/crop-recommendation-system

### Features:
- Nitrogen (N)  
- Phosphorus (P)  
- Potassium (K)  
- Temperature (°C)  
- Humidity (%)  
- pH value  
- Rainfall (mm)  

### Target:
- Crop label (e.g., rice, wheat, maize, etc.)


---

##  Steps  

### Download Dataset  
- Download from the above link  
- Extract the files
- 3. Place the dataset inside the folder:

```
Crop_recommendation dataset /
``` 

---

##  Installation & Setup  

### 1️ Clone the Repository  
```bash
git clone https://github.com/ashnajbn/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```

### 2️ Install Required Libraries
```bash
pip install -r requirements.txt
```

### 3️🚀 Launch the Mobile-Friendly App

#### Option A: Local Development
```bash
streamlit run streamlit_app.py
# Opens at http://localhost:8501
```

#### Option B: Access from Mobile Device (Same Network)
```bash
streamlit run streamlit_app.py --server.headless true
# Access from mobile: http://YOUR_COMPUTER_IP:8501
```

#### Option C: Deploy to Streamlit Cloud (Recommended for Production)
1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Deploy directly from GitHub repository
4. Share public link with farmers

### 4️ Run the Jupyter Notebook
```bash
jupyter notebook "Crop_Recommendation_System.ipynb"
```

---

## 📱 Mobile App Features

### Three Easy-to-Use Tabs:
1. **⚡ Quick Input** - Manual data entry with presets
2. **🌍 Weather** - Location-based recommendations
3. **📤 Bulk** - Upload and process multiple farms

### Mobile-Optimized Features:
✅ Responsive design for all screen sizes  
✅ Touch-friendly buttons (48px minimum)  
✅ Simple, intuitive interface  
✅ Fast predictions (< 1 second)  
✅ Works on iOS and Android  
✅ Accessible in bright sunlight  
✅ No complex navigation  

### Documentation:
- 📖 **[MOBILE_GUIDE.md](MOBILE_GUIDE.md)** - User guide for farmers
- 🔧 **[MOBILE_TECHNICAL.md](MOBILE_TECHNICAL.md)** - Technical specifications

---
## Technologies Used

- **Python** - Core programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine Learning models
- **Joblib** - Model serialization
- **Streamlit** - Mobile-friendly web interface
- **Requests** - Weather API integration
- **Matplotlib & Seaborn** - Data visualization

---

## Model Workflow

* Load dataset
* Perform data preprocessing
* Conduct Exploratory Data Analysis (EDA)
* Split dataset into training and testing sets
* Train Machine Learning models (e.g., Decision Tree, Random Forest)
* Evaluate model performance
* Predict suitable crops based on input parameters

---

## Future Improvements

- ✅ **Mobile-friendly interface** - COMPLETED
- ✅ **Real-time weather API integration** - COMPLETED  
- ✅ **Web deployment (Streamlit)** - COMPLETED
- 🔄 Use Deep Learning models for better accuracy
- 🔄 Add PWA support for offline access
- 🔄 Native mobile app wrappers (iOS/Android)
- 🔄 Voice input support for accessibility
- 🔄 Image-based soil analysis (camera input)
- 🔄 Multi-language support
- 🔄 Region-specific crop optimization
- 🔄 Push notifications for optimal farming times

---
## Authors

ANANTHAN S, 
ASHNA JEBIN, 
JEEVA B S






