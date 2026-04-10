# Region-Specific Crop Optimization Database

import pandas as pd

# Define regional data with crop preferences and optimal conditions
REGIONS = {
    "🏙️ North India": {
        "states": ["Punjab", "Haryana", "Himachal Pradesh", "Uttarakhand", "Jammu & Kashmir"],
        "climate": "Temperate",
        "rainfall": "400-1500 mm",
        "avg_temperature": "15-25°C",
        "soil_types": ["Alluvial", "Loamy"],
        "suitable_crops": {
            "Rice": 90,
            "Wheat": 95,
            "Maize": 85,
            "Potato": 88,
            "Sugarcane": 75,
            "Cotton": 60,
            "Groundnut": 55
        },
        "seasonal_crops": {
            "Rabi (Oct-Mar)": ["Wheat", "Barley", "Gram", "Linseed"],
            "Kharif (Jun-Oct)": ["Rice", "Maize", "Sugarcane", "Groundnut"]
        },
        "optimal_nitrogen": 80,
        "optimal_phosphorus": 40,
        "optimal_potassium": 40,
        "optimal_ph": 7.0,
        "tips": [
            "🌾 Best time for wheat: October-November",
            "💧 Ensure proper irrigation for rice",
            "🌱 Use nitrogen-rich fertilizers for maize",
            "❄️ Protect crops from frost in winter"
        ]
    },
    
    "🌊 South India": {
        "states": ["Karnataka", "Tamil Nadu", "Andhra Pradesh", "Telangana", "Kerala"],
        "climate": "Tropical/Sub-tropical",
        "rainfall": "600-2500 mm",
        "avg_temperature": "20-30°C",
        "soil_types": ["Black Soil", "Red Soil", "Laterite"],
        "suitable_crops": {
            "Rice": 85,
            "Sugarcane": 90,
            "Cotton": 88,
            "Coconut": 92,
            "Groundnut": 85,
            "Maize": 80,
            "Wheat": 60
        },
        "seasonal_crops": {
            "Southwest Monsoon (Jun-Sep)": ["Rice", "Coconut", "Sugarcane"],
            "Northeast Monsoon (Oct-Dec)": ["Groundnut", "Cotton", "Maize"]
        },
        "optimal_nitrogen": 90,
        "optimal_phosphorus": 45,
        "optimal_potassium": 50,
        "optimal_ph": 6.5,
        "tips": [
            "🌧️ Utilize monsoon rains for crop cultivation",
            "🥥 Coconut fields need well-drained soil",
            "🎯 Space plantations properly for air circulation",
            "☀️ Protect young plants from intense sun"
        ]
    },
    
    "🌄 Eastern India": {
        "states": ["West Bengal", "Bihar", "Jharkhand", "Odisha", "Assam"],
        "climate": "Sub-tropical",
        "rainfall": "1400-2300 mm",
        "avg_temperature": "18-28°C",
        "soil_types": ["Alluvial", "Laterite", "Acidic"],
        "suitable_crops": {
            "Rice": 95,
            "Wheat": 75,
            "Potato": 85,
            "Sugarcane": 80,
            "Jute": 90,
            "Maize": 80,
            "Groundnut": 65
        },
        "seasonal_crops": {
            "Rabi (Oct-Mar)": ["Wheat", "Potato", "Pulses"],
            "Kharif (Jun-Oct)": ["Rice", "Jute", "Sugarcane"]
        },
        "optimal_nitrogen": 85,
        "optimal_phosphorus": 45,
        "optimal_potassium": 45,
        "optimal_ph": 6.8,
        "tips": [
            "🌾 Rice is the main crop - excellent growing conditions",
            "🥔 Potato farming is highly profitable in this region",
            "💧 Manage waterlogging in monsoon season",
            "🌾 Use jute cultivation for additional income"
        ]
    },
    
    "🏜️ Western India": {
        "states": ["Gujarat", "Rajasthan", "Maharashtra"],
        "climate": "Semi-arid/Arid",
        "rainfall": "400-1000 mm",
        "avg_temperature": "20-35°C",
        "soil_types": ["Sandy", "Loamy", "Black Soil"],
        "suitable_crops": {
            "Groundnut": 92,
            "Cotton": 90,
            "Sugarcane": 85,
            "Maize": 80,
            "Wheat": 75,
            "Potato": 70,
            "Rice": 60
        },
        "seasonal_crops": {
            "Rabi (Oct-Mar)": ["Wheat", "Gram", "Barley"],
            "Kharif (Jun-Oct)": ["Cotton", "Groundnut", "Sugarcane"]
        },
        "optimal_nitrogen": 75,
        "optimal_phosphorus": 50,
        "optimal_potassium": 40,
        "optimal_ph": 7.2,
        "tips": [
            "🥜 Groundnut thrives in this climate",
            "🌾 Cotton is a major cash crop",
            "💧 Water conservation is critical",
            "🌱 Use drought-resistant varieties"
        ]
    },
    
    "🌲 Central India": {
        "states": ["Madhya Pradesh", "Chhattisgarh"],
        "climate": "Sub-humid",
        "rainfall": "1000-1500 mm",
        "avg_temperature": "15-30°C",
        "soil_types": ["Black Soil", "Red Soil", "Laterite"],
        "suitable_crops": {
            "Rice": 85,
            "Sugarcane": 85,
            "Wheat": 80,
            "Soybean": 90,
            "Cotton": 80,
            "Groundnut": 75,
            "Maize": 85
        },
        "seasonal_crops": {
            "Rabi (Oct-Mar)": ["Wheat", "Gram", "Soybean"],
            "Kharif (Jun-Oct)": ["Rice", "Maize", "Sugarcane"]
        },
        "optimal_nitrogen": 80,
        "optimal_phosphorus": 45,
        "optimal_potassium": 45,
        "optimal_ph": 6.8,
        "tips": [
            "🫘 Soybean is emerging as profitable crop",
            "🌾 Black soil region - excellent for multiple crops",
            "💧 Balanced rainfall supports diverse cultivation",
            "🌱 Crop rotation recommended for soil health"
        ]
    },
    
    "⛰️ Hilly Regions": {
        "states": ["Himachal Pradesh", "Uttarakhand", "Nilgiris", "Meghalaya"],
        "climate": "Temperate/Cool",
        "rainfall": "1500-2500 mm",
        "avg_temperature": "8-20°C",
        "soil_types": ["Loamy", "Sandy Loam", "Forest Soil"],
        "suitable_crops": {
            "Potato": 95,
            "Apple": 90,
            "Maize": 80,
            "Wheat": 85,
            "Barley": 85,
            "Tea": 85,
            "Almonds": 80
        },
        "seasonal_crops": {
            "Summer (Mar-Jun)": ["Potato", "Maize"],
            "Winter (Oct-Feb)": ["Wheat", "Barley"]
        },
        "optimal_nitrogen": 70,
        "optimal_phosphorus": 40,
        "optimal_potassium": 45,
        "optimal_ph": 6.2,
        "tips": [
            "🍎 Fruit cultivation is excellent in hilly areas",
            "🥔 Potato yields are exceptionally high",
            "⛰️ Terracing prevents soil erosion",
            "❄️ Cold-resistant varieties perform better"
        ]
    }
}

# Crop characteristics database
CROP_DATA = {
    "Rice": {
        "water_requirement": "1200-1500 mm",
        "temperature": "20-30°C",
        "soil_ph": "6.0-7.0",
        "duration": "120-150 days",
        "yield_potential": "4-6 tons/ha",
        "regions": ["North India", "South India", "Eastern India", "Central India"],
        "icon": "🌾"
    },
    "Wheat": {
        "water_requirement": "400-500 mm",
        "temperature": "15-25°C",
        "soil_ph": "6.5-7.5",
        "duration": "120-140 days",
        "yield_potential": "3-5 tons/ha",
        "regions": ["North India", "Central India", "Eastern India", "Western India"],
        "icon": "🌾"
    },
    "Cotton": {
        "water_requirement": "600-1000 mm",
        "temperature": "20-30°C",
        "soil_ph": "6.0-7.5",
        "duration": "160-180 days",
        "yield_potential": "2-3 tons/ha",
        "regions": ["South India", "Western India", "Central India"],
        "icon": "🎡"
    },
    "Sugarcane": {
        "water_requirement": "1500-2250 mm",
        "temperature": "20-30°C",
        "soil_ph": "6.0-8.0",
        "duration": "12-18 months",
        "yield_potential": "50-80 tons/ha",
        "regions": ["North India", "South India", "Eastern India", "Central India"],
        "icon": "🌾"
    },
    "Groundnut": {
        "water_requirement": "400-600 mm",
        "temperature": "20-30°C",
        "soil_ph": "5.9-7.3",
        "duration": "90-120 days",
        "yield_potential": "2.5-3.5 tons/ha",
        "regions": ["South India", "Western India", "Central India"],
        "icon": "🥜"
    },
    "Maize": {
        "water_requirement": "500-700 mm",
        "temperature": "21-27°C",
        "soil_ph": "6.0-7.5",
        "duration": "80-120 days",
        "yield_potential": "4-6 tons/ha",
        "regions": ["North India", "Western India", "Central India", "Hilly Regions"],
        "icon": "🌽"
    },
    "Potato": {
        "water_requirement": "400-600 mm",
        "temperature": "15-25°C",
        "soil_ph": "6.0-7.0",
        "duration": "70-120 days",
        "yield_potential": "20-25 tons/ha",
        "regions": ["North India", "Eastern India", "Hilly Regions"],
        "icon": "🥔"
    },
    "Coconut": {
        "water_requirement": "1400-2300 mm",
        "temperature": "20-30°C",
        "soil_ph": "5.5-8.0",
        "duration": "12 years bearing",
        "yield_potential": "40-80 nuts/tree/year",
        "regions": ["South India"],
        "icon": "🥥"
    },
    "Apple": {
        "water_requirement": "600-1000 mm",
        "temperature": "8-25°C",
        "soil_ph": "6.0-7.5",
        "duration": "4-5 years bearing",
        "yield_potential": "15-35 tons/ha",
        "regions": ["Hilly Regions", "North India"],
        "icon": "🍎"
    },
    "Tea": {
        "water_requirement": "1500-2250 mm",
        "temperature": "15-30°C",
        "soil_ph": "4.5-6.5",
        "duration": "3-4 years bearing",
        "yield_potential": "2-3 tons/ha (dried)",
        "regions": ["Hilly Regions", "South India"],
        "icon": "🍵"
    }
}

def get_region_data(region_name):
    """Get all data for a specific region"""
    return REGIONS.get(region_name, {})

def get_regional_crop_scores(region_name):
    """Get crop suitability scores for a region"""
    region = REGIONS.get(region_name, {})
    return region.get("suitable_crops", {})

def get_regional_optimal_conditions(region_name):
    """Get optimal soil/climate conditions for a region"""
    region = REGIONS.get(region_name, {})
    return {
        "nitrogen": region.get("optimal_nitrogen", 80),
        "phosphorus": region.get("optimal_phosphorus", 45),
        "potassium": region.get("optimal_potassium", 45),
        "ph": region.get("optimal_ph", 6.8)
    }

def get_crop_recommendation_boost(selected_crop, region_name):
    """Get confidence boost for a crop based on region suitability"""
    crop_scores = get_regional_crop_scores(region_name)
    return crop_scores.get(selected_crop, 50) / 100

def get_regional_tips(region_name):
    """Get farming tips for a specific region"""
    region = REGIONS.get(region_name, {})
    return region.get("tips", [])

def get_seasonal_crops(region_name):
    """Get seasonal crops for a region"""
    region = REGIONS.get(region_name, {})
    return region.get("seasonal_crops", {})

def get_crop_info(crop_name):
    """Get detailed information about a crop"""
    return CROP_DATA.get(crop_name, {})

def adjust_recommendation_for_region(base_score, crop_name, region_name, input_conditions):
    """
    Adjust the recommendation score based on regional factors
    
    Returns: adjusted_score, region_factor, tips
    """
    crop_scores = get_regional_crop_scores(region_name)
    regional_boost = crop_scores.get(crop_name, 50) / 100  # 0.5 to 1.0
    
    optimal_conditions = get_regional_optimal_conditions(region_name)
    
    # Calculate how well input conditions match regional optimals
    n_match = 1 - (abs(input_conditions['nitrogen'] - optimal_conditions['nitrogen']) / 200)
    p_match = 1 - (abs(input_conditions['phosphorus'] - optimal_conditions['phosphorus']) / 150)
    k_match = 1 - (abs(input_conditions['potassium'] - optimal_conditions['potassium']) / 200)
    ph_match = 1 - (abs(input_conditions['ph'] - optimal_conditions['ph']) / 4)
    
    condition_match = (n_match + p_match + k_match + ph_match) / 4  # Average match
    condition_match = max(0, condition_match)  # Ensure non-negative
    
    # Final adjustment
    region_adjustment_factor = (regional_boost + condition_match) / 2
    adjusted_score = base_score * region_adjustment_factor
    
    tips = get_regional_tips(region_name)
    
    return adjusted_score, region_adjustment_factor, tips

# List of available regions
REGION_LIST = list(REGIONS.keys())
