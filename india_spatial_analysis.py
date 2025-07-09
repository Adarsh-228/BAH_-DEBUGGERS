from flask import Blueprint, request, jsonify
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon
import json
import io
import base64
import folium
from folium import plugins
import numpy as np

india_spatial_bp = Blueprint('india_spatial', __name__)

class IndiaChainOfThoughtAnalyzer:
    """Chain-of-thought reasoning for Indian spatial analysis tasks"""
    
    def __init__(self):
        self.analysis_steps = []
        
    def decompose_task(self, user_query):
        """Break down user query into India-specific spatial analysis steps"""
        steps = []
        
        # India-specific keyword-based task decomposition
        query_lower = user_query.lower()
        
        if 'monsoon' in query_lower or 'rainfall' in query_lower:
            steps.append({
                'step': 1,
                'action': 'monsoon_analysis',
                'description': 'Analyze monsoon patterns and rainfall distribution',
                'reasoning': 'Monsoon analysis is crucial for Indian agriculture and water resource management'
            })
            
        if 'agriculture' in query_lower or 'crop' in query_lower or 'farming' in query_lower:
            steps.append({
                'step': len(steps) + 1,
                'action': 'agricultural_analysis',
                'description': 'Analyze agricultural patterns and crop distribution',
                'reasoning': 'Agricultural analysis helps optimize farming practices and food security in India'
            })
            
        if 'urban' in query_lower or 'city' in query_lower or 'metro' in query_lower:
            steps.append({
                'step': len(steps) + 1,
                'action': 'urban_planning_analysis',
                'description': 'Analyze urban growth and infrastructure patterns',
                'reasoning': 'Urban planning analysis is essential for managing India\'s rapid urbanization'
            })
            
        if 'pollution' in query_lower or 'air quality' in query_lower:
            steps.append({
                'step': len(steps) + 1,
                'action': 'pollution_analysis',
                'description': 'Analyze air pollution and environmental quality',
                'reasoning': 'Pollution analysis helps address environmental challenges in Indian cities'
            })
            
        if 'flood' in query_lower or 'disaster' in query_lower:
            steps.append({
                'step': len(steps) + 1,
                'action': 'disaster_risk_analysis',
                'description': 'Analyze flood risk and disaster vulnerability',
                'reasoning': 'Disaster risk analysis is critical for India\'s flood-prone regions'
            })
            
        if 'population' in query_lower or 'demographic' in query_lower:
            steps.append({
                'step': len(steps) + 1,
                'action': 'demographic_analysis',
                'description': 'Analyze population distribution and demographic patterns',
                'reasoning': 'Demographic analysis helps understand India\'s diverse population distribution'
            })
            
        if 'transport' in query_lower or 'railway' in query_lower or 'highway' in query_lower:
            steps.append({
                'step': len(steps) + 1,
                'action': 'transportation_analysis',
                'description': 'Analyze transportation networks and connectivity',
                'reasoning': 'Transportation analysis is vital for India\'s infrastructure development'
            })
            
        # Default India-focused analysis if no specific keywords found
        if not steps:
            steps = [
                {
                    'step': 1,
                    'action': 'india_data_exploration',
                    'description': 'Explore Indian geographic and demographic data',
                    'reasoning': 'Understanding India\'s diverse geography is the foundation of spatial analysis'
                },
                {
                    'step': 2,
                    'action': 'regional_pattern_analysis',
                    'description': 'Identify regional patterns across Indian states',
                    'reasoning': 'Regional analysis helps understand India\'s spatial diversity'
                }
            ]
            
        return steps
    
    def execute_analysis(self, steps, sample_data=True):
        """Execute the analysis steps and generate India-specific results"""
        results = []
        
        for step in steps:
            if sample_data:
                # Generate sample results for demonstration
                result = self._generate_india_sample_result(step)
            else:
                # Execute actual analysis (would require real data)
                result = self._execute_real_analysis(step)
                
            results.append(result)
            
        return results
    
    def _generate_india_sample_result(self, step):
        """Generate sample analysis results for Indian context"""
        action = step['action']
        
        if action == 'monsoon_analysis':
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'southwest_monsoon_coverage': 85.2,  # percentage
                    'average_rainfall_mm': 1200,
                    'drought_affected_districts': 45,
                    'flood_risk_areas': 12,
                    'agricultural_impact_score': 7.8
                },
                'explanation': 'Southwest monsoon covers 85.2% of India with 1200mm average rainfall. 45 districts face drought risk.'
            }
            
        elif action == 'agricultural_analysis':
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'rice_cultivation_area': 44.0,  # million hectares
                    'wheat_cultivation_area': 31.0,
                    'crop_productivity_index': 6.5,
                    'irrigation_coverage': 48.0,  # percentage
                    'organic_farming_adoption': 2.8
                },
                'explanation': 'Rice covers 44M hectares, wheat 31M hectares. Irrigation covers 48% of agricultural land.'
            }
            
        elif action == 'urban_planning_analysis':
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'urban_population_percentage': 34.9,
                    'metro_cities_count': 8,
                    'slum_population_millions': 65,
                    'green_cover_percentage': 12.3,
                    'infrastructure_development_score': 6.2
                },
                'explanation': '34.9% urban population across 8 metro cities. 65M people in slums, 12.3% green cover.'
            }
            
        elif action == 'pollution_analysis':
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'aqi_delhi': 168,  # Air Quality Index
                    'aqi_mumbai': 145,
                    'aqi_kolkata': 152,
                    'cities_exceeding_who_limits': 22,
                    'pm25_annual_average': 58.0  # μg/m³
                },
                'explanation': 'Delhi AQI: 168, Mumbai: 145. 22 cities exceed WHO air quality limits.'
            }
            
        elif action == 'disaster_risk_analysis':
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'flood_prone_districts': 89,
                    'cyclone_affected_coastal_length': 7516,  # km
                    'earthquake_high_risk_zones': 11,
                    'drought_vulnerable_area_percentage': 68,
                    'disaster_preparedness_score': 5.8
                },
                'explanation': '89 districts flood-prone, 7516km cyclone-affected coast. 68% area drought-vulnerable.'
            }
            
        elif action == 'demographic_analysis':
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'total_population_billions': 1.42,
                    'population_density_per_km2': 464,
                    'literacy_rate_percentage': 77.7,
                    'rural_population_percentage': 65.1,
                    'youth_population_percentage': 27.9
                },
                'explanation': '1.42B population, 464/km² density. 77.7% literacy, 65.1% rural, 27.9% youth.'
            }
            
        elif action == 'transportation_analysis':
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'railway_network_km': 68043,
                    'highway_network_km': 142126,
                    'airports_count': 148,
                    'major_ports': 12,
                    'connectivity_index': 6.7
                },
                'explanation': '68,043km railway, 142,126km highway network. 148 airports, 12 major ports.'
            }
            
        else:
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'status': 'completed',
                    'indian_states_analyzed': 28,
                    'union_territories_analyzed': 8,
                    'processing_time': 3.2
                },
                'explanation': f'Successfully completed {action} across 28 states and 8 union territories'
            }
    
    def _execute_real_analysis(self, step):
        """Execute real spatial analysis (placeholder for actual implementation)"""
        # This would contain actual geoprocessing logic with real Indian data
        pass

def create_india_sample_map():
    """Create a sample map focused on India with spatial analysis results"""
    # Create a map centered on India
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
    
    # Add major Indian cities
    indian_cities = [
        {'lat': 28.6139, 'lon': 77.2090, 'name': 'New Delhi', 'population': 32.9, 'type': 'capital'},
        {'lat': 19.0760, 'lon': 72.8777, 'name': 'Mumbai', 'population': 20.4, 'type': 'financial'},
        {'lat': 12.9716, 'lon': 77.5946, 'name': 'Bangalore', 'population': 13.2, 'type': 'tech'},
        {'lat': 22.5726, 'lon': 88.3639, 'name': 'Kolkata', 'population': 14.9, 'type': 'cultural'},
        {'lat': 13.0827, 'lon': 80.2707, 'name': 'Chennai', 'population': 11.5, 'type': 'industrial'},
        {'lat': 17.3850, 'lon': 78.4867, 'name': 'Hyderabad', 'population': 10.5, 'type': 'tech'},
        {'lat': 23.0225, 'lon': 72.5714, 'name': 'Ahmedabad', 'population': 8.4, 'type': 'commercial'},
        {'lat': 18.5204, 'lon': 73.8567, 'name': 'Pune', 'population': 7.4, 'type': 'education'}
    ]
    
    # Color coding for different city types
    city_colors = {
        'capital': 'red',
        'financial': 'blue',
        'tech': 'green',
        'cultural': 'purple',
        'industrial': 'orange',
        'commercial': 'darkblue',
        'education': 'darkgreen'
    }
    
    for city in indian_cities:
        folium.CircleMarker(
            location=[city['lat'], city['lon']],
            radius=city['population'],
            popup=f"<b>{city['name']}</b><br>Population: {city['population']}M<br>Type: {city['type'].title()}",
            color=city_colors[city['type']],
            fill=True,
            fillColor=city_colors[city['type']],
            fillOpacity=0.7,
            weight=2
        ).add_to(m)
    
    # Add sample agricultural regions
    agricultural_regions = [
        {'lat': 30.7333, 'lon': 76.7794, 'name': 'Punjab - Wheat Belt', 'crop': 'Wheat'},
        {'lat': 26.9124, 'lon': 75.7873, 'name': 'Rajasthan - Millet Region', 'crop': 'Millet'},
        {'lat': 11.1271, 'lon': 78.6569, 'name': 'Tamil Nadu - Rice Region', 'crop': 'Rice'},
        {'lat': 15.9129, 'lon': 79.7400, 'name': 'Andhra Pradesh - Cotton Belt', 'crop': 'Cotton'}
    ]
    
    for region in agricultural_regions:
        folium.Marker(
            location=[region['lat'], region['lon']],
            popup=f"<b>{region['name']}</b><br>Primary Crop: {region['crop']}",
            icon=folium.Icon(color='green', icon='leaf', prefix='fa')
        ).add_to(m)
    
    # Add monsoon analysis overlay
    monsoon_regions = [
        {'lat': 10.8505, 'lon': 76.2711, 'name': 'Kerala - High Rainfall', 'rainfall': 3000},
        {'lat': 26.2389, 'lon': 73.0243, 'name': 'Rajasthan - Low Rainfall', 'rainfall': 300},
        {'lat': 25.0961, 'lon': 85.3131, 'name': 'Bihar - Moderate Rainfall', 'rainfall': 1200}
    ]
    
    for region in monsoon_regions:
        # Color based on rainfall intensity
        if region['rainfall'] > 2000:
            color = 'darkblue'
        elif region['rainfall'] > 1000:
            color = 'blue'
        else:
            color = 'lightblue'
            
        folium.CircleMarker(
            location=[region['lat'], region['lon']],
            radius=15,
            popup=f"<b>{region['name']}</b><br>Annual Rainfall: {region['rainfall']}mm",
            color=color,
            fill=True,
            fillColor=color,
            fillOpacity=0.6
        ).add_to(m)
    
    # Convert map to HTML string
    map_html = m._repr_html_()
    
    return map_html

@india_spatial_bp.route('/analyze', methods=['POST'])
def analyze_india_spatial_data():
    """Main endpoint for India-specific spatial analysis requests"""
    try:
        data = request.get_json()
        user_query = data.get('query', '')
        
        if not user_query:
            return jsonify({'error': 'Query is required'}), 400
        
        # Initialize India-specific chain-of-thought analyzer
        analyzer = IndiaChainOfThoughtAnalyzer()
        
        # Decompose the task
        analysis_steps = analyzer.decompose_task(user_query)
        
        # Execute analysis
        results = analyzer.execute_analysis(analysis_steps)
        
        # Generate India-focused map visualization
        map_html = create_india_sample_map()
        
        response = {
            'query': user_query,
            'chain_of_thought': analysis_steps,
            'results': results,
            'map_html': map_html,
            'summary': f"Completed {len(analysis_steps)} India-specific analysis steps for: {user_query}",
            'country_focus': 'India',
            'geographic_scope': 'Indian subcontinent'
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@india_spatial_bp.route('/tools', methods=['GET'])
def get_india_spatial_tools():
    """Get list of India-specific spatial analysis tools"""
    tools = [
        {
            'name': 'Monsoon Analysis',
            'description': 'Analyze monsoon patterns and rainfall distribution across India',
            'parameters': ['season', 'region', 'year_range'],
            'use_cases': ['Agriculture planning', 'Water resource management', 'Flood prediction']
        },
        {
            'name': 'Agricultural Analysis',
            'description': 'Analyze crop patterns and agricultural productivity',
            'parameters': ['crop_type', 'state', 'season'],
            'use_cases': ['Crop yield prediction', 'Food security assessment', 'Irrigation planning']
        },
        {
            'name': 'Urban Planning Analysis',
            'description': 'Analyze urban growth and infrastructure in Indian cities',
            'parameters': ['city', 'infrastructure_type', 'time_period'],
            'use_cases': ['Smart city development', 'Slum rehabilitation', 'Transport planning']
        },
        {
            'name': 'Pollution Analysis',
            'description': 'Analyze air and water pollution across Indian regions',
            'parameters': ['pollution_type', 'city', 'monitoring_period'],
            'use_cases': ['Environmental monitoring', 'Health impact assessment', 'Policy planning']
        },
        {
            'name': 'Disaster Risk Analysis',
            'description': 'Analyze flood, cyclone, and earthquake risks',
            'parameters': ['disaster_type', 'region', 'vulnerability_factors'],
            'use_cases': ['Disaster preparedness', 'Insurance planning', 'Infrastructure resilience']
        },
        {
            'name': 'Demographic Analysis',
            'description': 'Analyze population distribution and demographic trends',
            'parameters': ['demographic_indicator', 'administrative_level', 'census_year'],
            'use_cases': ['Resource allocation', 'Development planning', 'Electoral analysis']
        }
    ]
    
    return jsonify({'tools': tools, 'country_focus': 'India'})

@india_spatial_bp.route('/sample-data', methods=['GET'])
def get_india_sample_data():
    """Get sample Indian spatial data for testing"""
    # Create sample GeoJSON data for India
    sample_features = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [77.2090, 28.6139]
                },
                "properties": {
                    "name": "New Delhi",
                    "type": "capital_city",
                    "population": 32900000,
                    "state": "Delhi",
                    "aqi": 168
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [72.8777, 19.0760]
                },
                "properties": {
                    "name": "Mumbai",
                    "type": "financial_center",
                    "population": 20400000,
                    "state": "Maharashtra",
                    "aqi": 145
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [77.5946, 12.9716]
                },
                "properties": {
                    "name": "Bangalore",
                    "type": "tech_hub",
                    "population": 13200000,
                    "state": "Karnataka",
                    "aqi": 98
                }
            }
        ]
    }
    
    return jsonify(sample_features)

@india_spatial_bp.route('/states', methods=['GET'])
def get_indian_states():
    """Get list of Indian states and union territories"""
    states_data = {
        "states": [
            {"name": "Andhra Pradesh", "capital": "Amaravati", "area_km2": 162968},
            {"name": "Arunachal Pradesh", "capital": "Itanagar", "area_km2": 83743},
            {"name": "Assam", "capital": "Dispur", "area_km2": 78438},
            {"name": "Bihar", "capital": "Patna", "area_km2": 94163},
            {"name": "Chhattisgarh", "capital": "Raipur", "area_km2": 135192},
            {"name": "Goa", "capital": "Panaji", "area_km2": 3702},
            {"name": "Gujarat", "capital": "Gandhinagar", "area_km2": 196244},
            {"name": "Haryana", "capital": "Chandigarh", "area_km2": 44212},
            {"name": "Himachal Pradesh", "capital": "Shimla", "area_km2": 55673},
            {"name": "Jharkhand", "capital": "Ranchi", "area_km2": 79716},
            {"name": "Karnataka", "capital": "Bangalore", "area_km2": 191791},
            {"name": "Kerala", "capital": "Thiruvananthapuram", "area_km2": 38852},
            {"name": "Madhya Pradesh", "capital": "Bhopal", "area_km2": 308245},
            {"name": "Maharashtra", "capital": "Mumbai", "area_km2": 307713},
            {"name": "Manipur", "capital": "Imphal", "area_km2": 22327},
            {"name": "Meghalaya", "capital": "Shillong", "area_km2": 22429},
            {"name": "Mizoram", "capital": "Aizawl", "area_km2": 21081},
            {"name": "Nagaland", "capital": "Kohima", "area_km2": 16579},
            {"name": "Odisha", "capital": "Bhubaneswar", "area_km2": 155707},
            {"name": "Punjab", "capital": "Chandigarh", "area_km2": 50362},
            {"name": "Rajasthan", "capital": "Jaipur", "area_km2": 342239},
            {"name": "Sikkim", "capital": "Gangtok", "area_km2": 7096},
            {"name": "Tamil Nadu", "capital": "Chennai", "area_km2": 130060},
            {"name": "Telangana", "capital": "Hyderabad", "area_km2": 112077},
            {"name": "Tripura", "capital": "Agartala", "area_km2": 10486},
            {"name": "Uttar Pradesh", "capital": "Lucknow", "area_km2": 240928},
            {"name": "Uttarakhand", "capital": "Dehradun", "area_km2": 53483},
            {"name": "West Bengal", "capital": "Kolkata", "area_km2": 88752}
        ],
        "union_territories": [
            {"name": "Andaman and Nicobar Islands", "capital": "Port Blair"},
            {"name": "Chandigarh", "capital": "Chandigarh"},
            {"name": "Dadra and Nagar Haveli and Daman and Diu", "capital": "Daman"},
            {"name": "Delhi", "capital": "New Delhi"},
            {"name": "Jammu and Kashmir", "capital": "Srinagar (Summer), Jammu (Winter)"},
            {"name": "Ladakh", "capital": "Leh"},
            {"name": "Lakshadweep", "capital": "Kavaratti"},
            {"name": "Puducherry", "capital": "Puducherry"}
        ]
    }
    
    return jsonify(states_data)

@india_spatial_bp.route('/health', methods=['GET'])
def india_health_check():
    """Health check endpoint for India-specific service"""
    return jsonify({
        'status': 'healthy',
        'service': 'india-spatial-analysis-backend',
        'country_focus': 'India',
        'geographic_scope': 'Indian subcontinent',
        'gis_libraries': {
            'geopandas': 'available',
            'shapely': 'available',
            'folium': 'available'
        },
        'analysis_capabilities': [
            'monsoon_analysis',
            'agricultural_analysis', 
            'urban_planning_analysis',
            'pollution_analysis',
            'disaster_risk_analysis',
            'demographic_analysis'
        ]
    })

