# BHUGARBH - India Spatial Analysis Agent

## Overview

The India Spatial Analysis Agent is a Cursor-like IDE interface specifically designed for solving complex spatial analysis tasks through intelligent geoprocessing orchestration, with a focus on Indian geographic data, cities, and spatial analysis use cases relevant to Indian urban planning, agriculture, and environmental monitoring.

## ✨ Features

- **Cursor-like Interface**: Professional dark theme UI with a three-panel layout (sidebar, main content, chat).
- **India-Specific Focus**: All examples, sample data, and use cases are tailored for the Indian context.
- **Interactive Map**: Powered by Leaflet.js, centered on India, displaying various spatial data layers.
- **Chain-of-Thought Reasoning**: AI assistant breaks down complex spatial queries into logical, explainable steps.
- **Spatial Analysis Tools**: Includes capabilities for Monsoon Analysis, Agricultural Analysis, Urban Planning, Pollution Analysis, Disaster Risk Analysis, and Demographic Analysis, all with an Indian focus.
- **Real-time Interaction**: Chat interface for natural language queries and immediate analysis results.
- **Integrated Terminal**: Displays command-line style output of analysis processes.
- **File Explorer**: Simulated file system for spatial data and analysis scripts.

## 🛠️ Technologies Used

### Frontend
- **React**: For building the user interface.
- **Leaflet.js**: For interactive mapping and geospatial visualization.
- **Vite**: As the build tool for the React application.
- **CSS**: For styling and responsive design.

### Backend
- **Flask**: A Python web framework for the backend API.
- **GeoPandas**: For working with geospatial data in Python.
- **Shapely**: For geometric operations.
- **Folium**: For generating interactive maps from Python.
- **Flask-CORS**: For handling Cross-Origin Resource Sharing.

## 🚀 Setup Instructions

To set up and run the project locally, follow these steps:

### 1. Clone the Repository (Simulated)
In a real scenario, you would clone the repository. For this simulated environment, the project files are already in place.

### 2. Backend Setup

Navigate to the `spatial-analysis-backend` directory:

```bash
cd spatial-analysis-backend
```

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
# If requirements.txt is not present, install manually:
pip install Flask Flask-Cors geopandas shapely rasterio fiona pyproj folium
```

Run the Flask backend server:

```bash
python src/main.py
```

The backend server will run on `http://localhost:5000`.

### 3. Frontend Setup

Navigate to the `spatial-analysis-agent` directory:

```bash
cd spatial-analysis-agent
```

Install the Node.js dependencies:

```bash
npm install
# or if you prefer pnpm
pnpm install
```

Start the React development server:

```bash
npm run dev --host
```

The frontend application will be accessible at `http://localhost:5173`.
video prototype -
https://github.com/user-attachments/assets/e7c0808b-9135-4678-bf09-8df5779c6ccd

## 💡 Usage

1. **Access the Application**: Open your web browser and navigate to `http://localhost:5173`.
2. **Interact with AI Assistant**: Use the chat panel on the right to ask questions about India-specific spatial analysis tasks (e.g., 

