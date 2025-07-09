import React, { useEffect, useRef } from 'react'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

// Fix for default markers in Leaflet with Vite
delete L.Icon.Default.prototype._getIconUrl
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
})

const MapComponent = ({ analysisResults, centerLat = 20.5937, centerLng = 78.9629, zoom = 5, country = "India" }) => {
  const mapRef = useRef(null)
  const mapInstanceRef = useRef(null)

  useEffect(() => {
    if (!mapInstanceRef.current) {
      // Initialize map centered on India
      mapInstanceRef.current = L.map(mapRef.current).setView([centerLat, centerLng], zoom)

      // Add OpenStreetMap tiles
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
      }).addTo(mapInstanceRef.current)

      // Add major Indian cities
      const indianCities = [
        { lat: 28.6139, lng: 77.2090, name: 'New Delhi', population: '32.9M', type: 'capital' },
        { lat: 19.0760, lng: 72.8777, name: 'Mumbai', population: '20.4M', type: 'financial' },
        { lat: 12.9716, lng: 77.5946, name: 'Bangalore', population: '13.2M', type: 'tech' },
        { lat: 22.5726, lng: 88.3639, name: 'Kolkata', population: '14.9M', type: 'cultural' },
        { lat: 13.0827, lng: 80.2707, name: 'Chennai', population: '11.5M', type: 'industrial' },
        { lat: 17.3850, lng: 78.4867, name: 'Hyderabad', population: '10.5M', type: 'tech' },
        { lat: 23.0225, lng: 72.5714, name: 'Ahmedabad', population: '8.4M', type: 'commercial' },
        { lat: 18.5204, lng: 73.8567, name: 'Pune', population: '7.4M', type: 'education' }
      ]

      // Color coding for different city types
      const cityColors = {
        capital: '#dc2626',
        financial: '#2563eb', 
        tech: '#16a34a',
        cultural: '#9333ea',
        industrial: '#ea580c',
        commercial: '#1e40af',
        education: '#15803d'
      }

      indianCities.forEach(city => {
        const marker = L.circleMarker([city.lat, city.lng], {
          radius: 8,
          fillColor: cityColors[city.type],
          color: '#fff',
          weight: 2,
          opacity: 1,
          fillOpacity: 0.8
        }).addTo(mapInstanceRef.current)

        marker.bindPopup(`
          <div style="font-family: Arial, sans-serif;">
            <h3 style="margin: 0 0 8px 0; color: ${cityColors[city.type]};">${city.name}</h3>
            <p style="margin: 4px 0;"><strong>Population:</strong> ${city.population}</p>
            <p style="margin: 4px 0;"><strong>Type:</strong> ${city.type.charAt(0).toUpperCase() + city.type.slice(1)}</p>
          </div>
        `)
      })

      // Add sample agricultural regions
      const agriculturalRegions = [
        { lat: 30.7333, lng: 76.7794, name: 'Punjab - Wheat Belt', crop: 'Wheat', color: '#fbbf24' },
        { lat: 26.9124, lng: 75.7873, name: 'Rajasthan - Millet Region', crop: 'Millet', color: '#f59e0b' },
        { lat: 11.1271, lng: 78.6569, name: 'Tamil Nadu - Rice Region', crop: 'Rice', color: '#84cc16' },
        { lat: 15.9129, lng: 79.7400, name: 'Andhra Pradesh - Cotton Belt', crop: 'Cotton', color: '#f3f4f6' }
      ]

      agriculturalRegions.forEach(region => {
        const marker = L.marker([region.lat, region.lng], {
          icon: L.divIcon({
            className: 'custom-div-icon',
            html: `<div style="background-color: ${region.color}; width: 20px; height: 20px; border-radius: 50%; border: 2px solid #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.3);"></div>`,
            iconSize: [20, 20],
            iconAnchor: [10, 10]
          })
        }).addTo(mapInstanceRef.current)

        marker.bindPopup(`
          <div style="font-family: Arial, sans-serif;">
            <h3 style="margin: 0 0 8px 0; color: #16a34a;">${region.name}</h3>
            <p style="margin: 4px 0;"><strong>Primary Crop:</strong> ${region.crop}</p>
            <p style="margin: 4px 0;"><strong>Region:</strong> Agricultural Zone</p>
          </div>
        `)
      })

      // Add monsoon analysis overlay
      const monsoonRegions = [
        { lat: 10.8505, lng: 76.2711, name: 'Kerala - High Rainfall', rainfall: 3000, color: '#1e40af' },
        { lat: 26.2389, lng: 73.0243, name: 'Rajasthan - Low Rainfall', rainfall: 300, color: '#93c5fd' },
        { lat: 25.0961, lng: 85.3131, name: 'Bihar - Moderate Rainfall', rainfall: 1200, color: '#3b82f6' }
      ]

      monsoonRegions.forEach(region => {
        const circle = L.circle([region.lat, region.lng], {
          color: region.color,
          fillColor: region.color,
          fillOpacity: 0.3,
          radius: 50000
        }).addTo(mapInstanceRef.current)

        circle.bindPopup(`
          <div style="font-family: Arial, sans-serif;">
            <h3 style="margin: 0 0 8px 0; color: ${region.color};">${region.name}</h3>
            <p style="margin: 4px 0;"><strong>Annual Rainfall:</strong> ${region.rainfall}mm</p>
            <p style="margin: 4px 0;"><strong>Monsoon Impact:</strong> ${region.rainfall > 2000 ? 'High' : region.rainfall > 1000 ? 'Moderate' : 'Low'}</p>
          </div>
        `)
      })
    }

    // Update map with analysis results
    if (analysisResults && analysisResults.results) {
      // Clear previous analysis markers
      mapInstanceRef.current.eachLayer(layer => {
        if (layer.options && layer.options.analysisMarker) {
          mapInstanceRef.current.removeLayer(layer)
        }
      })

      // Add new analysis results
      analysisResults.results.forEach((result, index) => {
        if (result.action === 'monsoon_analysis') {
          // Add monsoon-specific markers
          const monsoonMarker = L.marker([19.7515, 75.7139], { // Maharashtra center
            icon: L.divIcon({
              className: 'analysis-marker',
              html: `<div style="background: #1e40af; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">Monsoon Analysis</div>`,
              iconSize: [120, 30],
              iconAnchor: [60, 15]
            }),
            analysisMarker: true
          }).addTo(mapInstanceRef.current)

          monsoonMarker.bindPopup(`
            <div style="font-family: Arial, sans-serif;">
              <h3 style="margin: 0 0 8px 0; color: #1e40af;">Monsoon Analysis Results</h3>
              <p><strong>SW Monsoon Coverage:</strong> ${result.result.southwest_monsoon_coverage}%</p>
              <p><strong>Average Rainfall:</strong> ${result.result.average_rainfall_mm}mm</p>
              <p><strong>Drought Affected Districts:</strong> ${result.result.drought_affected_districts}</p>
            </div>
          `)
        }

        if (result.action === 'agricultural_analysis') {
          // Add agricultural analysis markers
          const agriMarker = L.marker([18.5204, 73.8567], { // Pune area
            icon: L.divIcon({
              className: 'analysis-marker',
              html: `<div style="background: #16a34a; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">Agricultural Analysis</div>`,
              iconSize: [140, 30],
              iconAnchor: [70, 15]
            }),
            analysisMarker: true
          }).addTo(mapInstanceRef.current)

          agriMarker.bindPopup(`
            <div style="font-family: Arial, sans-serif;">
              <h3 style="margin: 0 0 8px 0; color: #16a34a;">Agricultural Analysis Results</h3>
              <p><strong>Rice Cultivation:</strong> ${result.result.rice_cultivation_area}M hectares</p>
              <p><strong>Wheat Cultivation:</strong> ${result.result.wheat_cultivation_area}M hectares</p>
              <p><strong>Irrigation Coverage:</strong> ${result.result.irrigation_coverage}%</p>
            </div>
          `)
        }
      })
    }

  }, [analysisResults, centerLat, centerLng, zoom])

  return (
    <div 
      ref={mapRef} 
      style={{ 
        height: '400px', 
        width: '100%', 
        border: '1px solid #374151',
        borderRadius: '8px'
      }} 
    />
  )
}

export default MapComponent

