# Crop Recommendation System 

A Machine Learning based Predictive Analytics Project  

## Crop Recommendation using Machine Learning  

## Project Overview  
This project focuses on building a **Crop Recommendation System** using Machine Learning techniques. The model suggests the most suitable crop to grow based on environmental and soil parameters such as **Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall**.

This system helps farmers and agricultural planners make **data-driven decisions** to improve productivity and optimize crop yield.

---

## Features  
-  Machine Learning-based crop recommendations
-  **Mobile-optimized responsive interface** for smartphones & tablets
-  **Region-specific crop optimization** (6 regions with customized recommendations)
-  Real-time weather API integration (OpenWeatherMap)
-  Interactive data visualization and analytics
-  Bulk prediction capability (CSV upload with regional adjustment)
-  Model caching for fast predictions
-  Secure, offline-capable predictions
-  Comprehensive accuracy metrics
-  Farmer-friendly UI with intuitive controls
-  Tab-based navigation for easy mobile access
-  Seasonal crop recommendations by region
-  Regional soil condition guidance (N, P, K, pH optimization)
-  Region-specific farming tips and best practices  

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

##  Dataset  
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

### 3️ Launch the Mobile-Friendly App

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

##  Mobile App Features

### Four Easy-to-Use Tabs:
1. **⚡ Quick Input** - Manual data entry with region selection & regional confidence adjustment
2. **🌍 Weather** - Location-based recommendations with regional optimization
3. **📤 Bulk** - Upload and process multiple farms with batch regional adjustment
4. **📍 Region Info** - View region-specific crop data, seasonal crops, and soil conditions

### Mobile-Optimized Features:
✅ Responsive design for all screen sizes (mobile-first, 500px max-width)  
✅ Touch-friendly buttons (48px minimum)  
✅ Simple, intuitive interface with region selector  
✅ Fast predictions (< 1 second)  
✅ Works on iOS and Android  
✅ Accessible in bright sunlight  
✅ No complex navigation  
✅ Region-aware recommendations  
✅ Seasonal crop guidance  
✅ Optimal soil condition display  

### Documentation:
-  **[MOBILE_GUIDE.md](MOBILE_GUIDE.md)** - User guide for farmers
-  **[MOBILE_TECHNICAL.md](MOBILE_TECHNICAL.md)** - Technical specifications
-  **[REGION_OPTIMIZATION.md](REGION_OPTIMIZATION.md)** - Region-specific recommendations guide
-  **[REGION_IMPLEMENTATION_SUMMARY.md](REGION_IMPLEMENTATION_SUMMARY.md)** - Complete technical overview

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

## Complete Workflow

### 1. Data Processing Pipeline
- Load dataset (22 crops, 2,200+ samples)
- Perform data preprocessing (normalization, encoding)
- Conduct Exploratory Data Analysis (EDA)
- Split dataset into training (80%) and testing (20%) sets

### 2. Model Training & Evaluation
- Train Machine Learning models (Random Forest, Decision Tree)
- Evaluate models using accuracy, precision, recall, F1-score
- Optimize hyperparameters for best performance
- Serialize models using joblib for production deployment

### 3. Prediction Pipeline
- Accept user input (N, P, K, Temperature, Humidity, pH, Rainfall)
- Load cached ML model and scaler
- Normalize input using fitted scaler
- Generate base crop prediction with confidence score

### 4. Regional Optimization Pipeline (NEW)
- Retrieve selected region from user interface
- Look up crop suitability score for recommended crop in selected region
- Compare input soil conditions (N, P, K, pH) to region's optimal levels
- Calculate regional adjustment factor (0.50-1.00)
- Apply adjustment: `Adjusted Confidence = Base Confidence × Regional Factor`
- Return region-specific tips and seasonal information

### 5. Batch Processing (Bulk Tab)
- Upload CSV with multiple farm records
- Apply ML prediction to each row
- Apply regional optimization to each prediction
- Generate summary statistics (base vs regional confidence)
- Export enhanced CSV with regional factors

### 6. Region Info Tab
- Display 6 predefined regions (North, South, East, West, Central, Hilly)
- Show climate, rainfall, temperature ranges for each region
- List suitable crops with color-coded suitability ratings (⭐-⭐⭐⭐)
- Display optimal soil conditions (N, P, K, pH) per region
- Show seasonal crops (Rabi, Kharif, Summer)
- Provide region-specific farming tips and best practices

---

## Project Status & Improvements

### ✅ Completed Features
- ✅ **Mobile-friendly interface** - Responsive design, 500px max-width, touch-optimized
- ✅ **Real-time weather API integration** - OpenWeatherMap integration with regional adjustments
- ✅ **Web deployment (Streamlit)** - Production-ready Streamlit Cloud deployment
- ✅ **Region-specific crop optimization** - 6 regions with 70+ data points, regional adjustment algorithm
- ✅ **Seasonal crop recommendations** - Region-specific seasonal crops (Rabi, Kharif, Summer)
- ✅ **Regional soil condition guidance** - Optimal N, P, K, pH by region
- ✅ **Bulk processing with regional adjustment** - Batch CSV upload with regional factors
- ✅ **Region Info dashboard** - Comprehensive regional data display for farmers

### 🔄 Future Enhancements  
- 🔄 Sub-district/block-level optimization (microclimate analysis)
- 🔄 Deep Learning models (LSTM, CNN) for improved accuracy
- 🔄 PWA support for offline access
- 🔄 Native mobile app wrappers (iOS/Android)
- 🔄 Voice input support for accessibility
- 🔄 Image-based soil analysis (camera input for soil color detection)
- 🔄 Multi-language support (Hindi, Regional languages)
- 🔄 Push notifications for optimal planting times
- 🔄 Price-based crop optimization (market demand integration)
- 🔄 Pest & disease regional pattern database
- 🔄 Climate change impact modeling

---

##  Region-Specific Optimization System

### Supported Regions (6 Regions)

| Region | Climate | Rainfall | Key Crops | Optimal N | States |
|--------|---------|----------|-----------|-----------|--------|
| **North India** | Temperate | 400-1500 mm | Wheat, Rice, Maize | 80 mg/kg | Punjab, Haryana, Uttar Pradesh, Himachal Pradesh, Jammu & Kashmir |
| **South India** | Tropical | 600-2500 mm | Coconut, Cotton, Sugarcane | 90 mg/kg | Karnataka, Tamil Nadu, Andhra Pradesh, Telangana, Kerala |
| **Eastern India** | Sub-tropical | 1400-2300 mm | Rice, Jute, Tea | 85 mg/kg | West Bengal, Assam, Odisha, Bihar, Jharkhand |
| **Western India** | Semi-arid | 400-1000 mm | Groundnut, Cotton, Bajra | 75 mg/kg | Gujarat, Rajasthan, Maharashtra, Goa |
| **Central India** | Sub-humid | 1000-1500 mm | Soybean, Rice, Chickpea | 80 mg/kg | Madhya Pradesh, Chhattisgarh |
| **Hilly Regions** | Temperate | 1500-2500 mm | Potato, Apple, Tea | 70 mg/kg | Uttarakhand, Himachal Pradesh, Meghalaya, Sikkim |

### Regional Adjustment Algorithm

The system calculates an **adjustment factor** by combining:
1. **Crop Suitability Score**: Region-specific appropriateness for recommended crop (0-100%)
2. **Condition Match**: How well input soil conditions match regional optimals (0-100%)
3. **Final Factor**: (Suitability + Condition Match) / 2 = 0.20-1.00
4. **Adjusted Confidence** = Base Confidence × Final Factor

**Example:**
- Base prediction: Wheat (85% confidence)
- Region: North India
- Wheat suitability in North: 95%
- Soil conditions match: 85%
- Regional factor: (95 + 85) / 2 = 90% → 0.90
- **Final confidence: 85% × 0.90 = 76.5%** ✓ Recommended

### Region-Specific Data Points

Each region includes:
-  Climate classification
-  Rainfall range (mm/year)
-  Temperature range (°C)
-  Soil types
-  Suitable crops (with suitability scores)
-  Seasonal crops (Rabi, Kharif, Summer)
-  Optimal nutrients (N, P, K, pH)
-  Regional farming tips & best practices

### Using Region Optimization

**Step 1:** Open the Streamlit app
```bash
streamlit run streamlit_app.py
```

**Step 2:** Choose Tab 1 (⚡ Quick Input) or Tab 2 (🌍 Weather)

**Step 3:** Select your region from the **Region Selector** dropdown

**Step 4:** Enter your soil/weather data

**Step 5:** Get region-optimized recommendation with:
- Base confidence score
- Regional adjustment factor
- Final adjusted confidence
- Seasonal crops for your region
- Optimal soil conditions
- Regional farming tips

---

##  System Architecture

### Technology Stack
```
Frontend: Streamlit + CSS3 (mobile-responsive)
Backend: Python with scikit-learn
Database: Region data (in-memory dict)
ML Model: Random Forest Classifier (joblib cached)
API: OpenWeatherMap (real-time weather)
Deployment: Streamlit Cloud / Docker
```

### File Structure
```
Crop-Recommendation-System/
├── streamlit_app.py                    # Main web application (4 tabs)
├── region_optimizer.py                 # Regional database & adjustment functions
├── Crop_Recommendation_System.ipynb    # ML model development notebook
├── requirements.txt                    # Python dependencies
├── Dockerfile                          # Docker containerization
├── README.md                           # Project documentation
├── DEPLOYMENT.md                       # Deployment instructions
├── RUN_APP.md                          # Quick start guide
│
├── 📁 Models/
│   ├── crop_recommendation_model.pkl   # Trained Random Forest
│   └── scaler.pkl                      # Feature scaler
│
└── 📁 Documentation/
    ├── MOBILE_GUIDE.md                 # User guide for farmers
    ├── MOBILE_TECHNICAL.md             # Mobile implementation details
    ├── MOBILE_SUMMARY.md               # Mobile project summary
    ├── REGION_OPTIMIZATION.md          # Region-specific guide
    └── REGION_IMPLEMENTATION_SUMMARY.md # Technical overview
```

### Data Flow

```
User Input (Soil/Weather Data)
    ↓
[Streamlit Interface]
    ↓
[ML Prediction - Random Forest]
    ↓
[Regional Lookup - region_optimizer.py]
    ↓
[Adjustment Calculation]
    ↓
[Output Display]
    ├─ Recommended Crop
    ├─ Base Confidence
    ├─ Regional Factor
    ├─ Final Confidence
    ├─ Seasonal Crops
    ├─ Optimal Soil Conditions
    └─ Regional Tips
```

---

##  Deployment Options

### Option 1: Local Development
```bash
# Clone repository
git clone https://github.com/ashnajbn/Crop-Recommendation-System-Using-Soil-and-Climate-Data.git
cd Crop-Recommendation-System-Using-Soil-and-Climate-Data

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run streamlit_app.py
```

### Option 2: Docker Containerization
```bash
# Build Docker image
docker build -t crop-recommendation:v1 .

# Run container
docker run -p 8501:8501 crop-recommendation:v1

# Access at http://localhost:8501
```

### Option 3: Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Click "New app" → Select your repository
4. Deploy automatically
5. Share public link with farmers
6. Auto-updates on each GitHub push

### Option 4: Network Access (Same Network)
```bash
# Get your computer's IP
ipconfig  # Windows
ifconfig  # Linux/Mac

# Run Streamlit
streamlit run streamlit_app.py

# Access from mobile: http://YOUR_IP:8501
```

See **[DEPLOYMENT.md](DEPLOYMENT.md)** for detailed deployment instructions.

---

##  Model Performance

- **Accuracy**: ~95% on test data
- **Precision**: 0.94 (average across crops)
- **Recall**: 0.93
- **F1-Score**: 0.93
- **Training Time**: ~2 seconds
- **Prediction Time**: <100ms per sample
- **Model Type**: Random Forest Classifier (100 trees)

---

##  How to Use

### For Farmers (Streamlit App)
1. **Quick Input Tab**: Manually enter soil parameters
   - N, P, K levels
   - Temperature, Humidity
   - pH, Rainfall
   - Select your region
   - Get crop recommendation!

2. **Weather Tab**: Location-based recommendations
   - Enter city name
   - Fetch real-time weather
   - System suggests crops matching weather
   - Regional optimization applied

3. **Bulk Tab**: Process multiple farms at once
   - Upload CSV with farm data
   - Select region
   - Get batch recommendations
   - Download results with regional factors

4. **Region Info Tab**: Learn about your region
   - View all suitable crops
   - Check seasonal crops
   - Learn optimal soil conditions
   - Read regional farming tips

### For Developers (Jupyter Notebook)
- Open `Crop_Recommendation_System.ipynb`
- Follow EDA, model training, and evaluation steps
- Customize ML models
- Retrain with your own data

---

##  Customization

### Add New Crops
Edit `region_optimizer.py`:
```python
"new_crop": {
    "water_requirement": "X mm",
    "temperature": "A-B°C",
    "soil_ph": "A.B-C.D",
    "duration": "X days",
    "yield_potential": "X tons/ha",
    "regions": ["North", "Central"]
}
```

### Add New Regions
Edit `region_optimizer.py` and add to `REGIONS` dictionary with required data fields.

### Retrain ML Model
1. Prepare new dataset with same features
2. Run training code in Jupyter notebook
3. Save updated model: `crop_recommendation_model.pkl`
4. Restart app: `streamlit run streamlit_app.py`

---

## 📖 Documentation

- 📘 **[README.md](README.md)** - Project overview & quick start
- 📕 **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deployment instructions
- 📗 **[RUN_APP.md](RUN_APP.md)** - Running the app locally
- 📙 **[MOBILE_GUIDE.md](MOBILE_GUIDE.md)** - Mobile app user guide (farmers)
- 📔 **[MOBILE_TECHNICAL.md](MOBILE_TECHNICAL.md)** - Mobile technical specs (developers)
- 📓 **[REGION_OPTIMIZATION.md](REGION_OPTIMIZATION.md)** - Regional recommendations guide
- 📒 **[REGION_IMPLEMENTATION_SUMMARY.md](REGION_IMPLEMENTATION_SUMMARY.md)** - Technical summary

---

## 💬 Support & Contact

For issues, questions, or suggestions:
- Open an issue on GitHub
- Email the development team
- Check documentation files for detailed guides

---

## 📄 License

This project is open source and available under the MIT License.

---

## Authors

ANANTHAN S  
ASHNA JABIN NK  
JEEVA B S

**Project**: Crop Recommendation System Using Soil and Climate Data  
**Version**: 2.1 (Region-Optimized with Mobile Interface)  
**Status**: Production Ready ✅  
**Last Updated**: April 2026






