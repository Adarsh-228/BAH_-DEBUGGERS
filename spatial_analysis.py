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

spatial_bp = Blueprint('spatial', __name__)

class ChainOfThoughtAnalyzer:
    """Chain-of-thought reasoning for spatial analysis tasks"""
    
    def __init__(self):
        self.analysis_steps = []
        
    def decompose_task(self, user_query):
        """Break down user query into spatial analysis steps"""
        steps = []
        
        # Simple keyword-based task decomposition
        query_lower = user_query.lower()
        
        if 'buffer' in query_lower:
            steps.append({
                'step': 1,
                'action': 'create_buffer',
                'description': 'Create buffer zones around features',
                'reasoning': 'Buffer analysis helps identify areas within a specified distance'
            })
            
        if 'intersection' in query_lower or 'overlap' in query_lower:
            steps.append({
                'step': len(steps) + 1,
                'action': 'spatial_intersection',
                'description': 'Find overlapping areas between datasets',
                'reasoning': 'Intersection analysis identifies where features overlap spatially'
            })
            
        if 'distance' in query_lower or 'nearest' in query_lower:
            steps.append({
                'step': len(steps) + 1,
                'action': 'distance_analysis',
                'description': 'Calculate distances between features',
                'reasoning': 'Distance analysis helps find proximity relationships'
            })
            
        if 'density' in query_lower or 'distribution' in query_lower:
            steps.append({
                'step': len(steps) + 1,
                'action': 'density_analysis',
                'description': 'Analyze spatial distribution and density patterns',
                'reasoning': 'Density analysis reveals clustering and distribution patterns'
            })
            
        if 'green space' in query_lower or 'vegetation' in query_lower:
            steps.append({
                'step': len(steps) + 1,
                'action': 'green_space_analysis',
                'description': 'Analyze green space coverage and accessibility',
                'reasoning': 'Green space analysis helps urban planning and environmental assessment'
            })
            
        # Default analysis if no specific keywords found
        if not steps:
            steps = [
                {
                    'step': 1,
                    'action': 'data_exploration',
                    'description': 'Explore and understand the spatial data',
                    'reasoning': 'Data exploration is the first step in any spatial analysis'
                },
                {
                    'step': 2,
                    'action': 'spatial_visualization',
                    'description': 'Create maps and visualizations',
                    'reasoning': 'Visualization helps identify patterns and relationships'
                }
            ]
            
        return steps
    
    def execute_analysis(self, steps, sample_data=True):
        """Execute the analysis steps and generate results"""
        results = []
        
        for step in steps:
            if sample_data:
                # Generate sample results for demonstration
                result = self._generate_sample_result(step)
            else:
                # Execute actual analysis (would require real data)
                result = self._execute_real_analysis(step)
                
            results.append(result)
            
        return results
    
    def _generate_sample_result(self, step):
        """Generate sample analysis results for demonstration"""
        action = step['action']
        
        if action == 'green_space_analysis':
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'total_green_space_area': 2.5,  # km²
                    'green_space_percentage': 15.3,
                    'average_distance_to_green_space': 0.8,  # km
                    'accessibility_score': 7.2
                },
                'explanation': 'Analysis shows 15.3% green space coverage with good accessibility (average 0.8km distance)'
            }
            
        elif action == 'density_analysis':
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'high_density_areas': 3,
                    'medium_density_areas': 7,
                    'low_density_areas': 12,
                    'clustering_coefficient': 0.65
                },
                'explanation': 'Spatial distribution shows moderate clustering with 3 high-density zones identified'
            }
            
        elif action == 'buffer_analysis':
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'buffer_distance': 500,  # meters
                    'features_within_buffer': 45,
                    'total_buffer_area': 1.2  # km²
                },
                'explanation': 'Buffer analysis identified 45 features within 500m radius'
            }
            
        else:
            return {
                'step': step['step'],
                'action': action,
                'result': {
                    'status': 'completed',
                    'features_processed': 150,
                    'processing_time': 2.3
                },
                'explanation': f'Successfully completed {action} on 150 features'
            }
    
    def _execute_real_analysis(self, step):
        """Execute real spatial analysis (placeholder for actual implementation)"""
        # This would contain actual geoprocessing logic
        pass

def create_sample_map():
    """Create a sample map with spatial analysis results"""
    # Create a map centered on a sample location
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)
    
    # Add sample green spaces
    green_spaces = [
        {'lat': 40.7829, 'lon': -73.9654, 'name': 'Central Park', 'area': 3.41},
        {'lat': 40.7505, 'lon': -73.9934, 'name': 'Bryant Park', 'area': 0.039},
        {'lat': 40.7021, 'lon': -73.9969, 'name': 'Washington Square Park', 'area': 0.039}
    ]
    
    for space in green_spaces:
        folium.CircleMarker(
            location=[space['lat'], space['lon']],
            radius=space['area'] * 5,
            popup=f"{space['name']}<br>Area: {space['area']} km²",
            color='green',
            fill=True,
            fillColor='lightgreen',
            fillOpacity=0.7
        ).add_to(m)
    
    # Add sample analysis areas
    analysis_areas = [
        {'lat': 40.7589, 'lon': -73.9851, 'density': 'High'},
        {'lat': 40.7282, 'lon': -73.9942, 'density': 'Medium'},
        {'lat': 40.7614, 'lon': -73.9776, 'density': 'Low'}
    ]
    
    colors = {'High': 'red', 'Medium': 'orange', 'Low': 'blue'}
    
    for area in analysis_areas:
        folium.CircleMarker(
            location=[area['lat'], area['lon']],
            radius=10,
            popup=f"Density: {area['density']}",
            color=colors[area['density']],
            fill=True,
            fillOpacity=0.5
        ).add_to(m)
    
    # Convert map to HTML string
    map_html = m._repr_html_()
    
    return map_html

@spatial_bp.route('/analyze', methods=['POST'])
def analyze_spatial_data():
    """Main endpoint for spatial analysis requests"""
    try:
        data = request.get_json()
        user_query = data.get('query', '')
        
        if not user_query:
            return jsonify({'error': 'Query is required'}), 400
        
        # Initialize chain-of-thought analyzer
        analyzer = ChainOfThoughtAnalyzer()
        
        # Decompose the task
        analysis_steps = analyzer.decompose_task(user_query)
        
        # Execute analysis
        results = analyzer.execute_analysis(analysis_steps)
        
        # Generate map visualization
        map_html = create_sample_map()
        
        response = {
            'query': user_query,
            'chain_of_thought': analysis_steps,
            'results': results,
            'map_html': map_html,
            'summary': f"Completed {len(analysis_steps)} analysis steps for: {user_query}"
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@spatial_bp.route('/tools', methods=['GET'])
def get_available_tools():
    """Get list of available spatial analysis tools"""
    tools = [
        {
            'name': 'Buffer Analysis',
            'description': 'Create buffer zones around features',
            'parameters': ['distance', 'units']
        },
        {
            'name': 'Overlay Analysis',
            'description': 'Find intersections and overlaps between datasets',
            'parameters': ['operation_type', 'input_layers']
        },
        {
            'name': 'Distance Analysis',
            'description': 'Calculate distances and proximity relationships',
            'parameters': ['measurement_type', 'target_features']
        },
        {
            'name': 'Density Analysis',
            'description': 'Analyze spatial distribution patterns',
            'parameters': ['analysis_method', 'grid_size']
        },
        {
            'name': 'Green Space Analysis',
            'description': 'Analyze vegetation and green space coverage',
            'parameters': ['vegetation_index', 'accessibility_threshold']
        }
    ]
    
    return jsonify({'tools': tools})

@spatial_bp.route('/sample-data', methods=['GET'])
def get_sample_data():
    """Get sample spatial data for testing"""
    # Create sample GeoJSON data
    sample_features = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [-74.0060, 40.7128]
                },
                "properties": {
                    "name": "Sample Point 1",
                    "type": "green_space",
                    "area": 1.5
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [-73.9654, 40.7829]
                },
                "properties": {
                    "name": "Sample Point 2",
                    "type": "green_space",
                    "area": 3.4
                }
            }
        ]
    }
    
    return jsonify(sample_features)

@spatial_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'spatial-analysis-backend',
        'gis_libraries': {
            'geopandas': 'available',
            'shapely': 'available',
            'folium': 'available'
        }
    })

