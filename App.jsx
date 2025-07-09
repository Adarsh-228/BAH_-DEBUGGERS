import { useState } from 'react'
import MapComponent from './components/MapComponent'
import './App.css'

function App() {
  const [analysisResults, setAnalysisResults] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [chatMessages, setChatMessages] = useState([
    {
      type: 'user',
      content: 'I need to analyze monsoon patterns and agricultural productivity in Maharashtra state'
    },
    {
      type: 'assistant', 
      content: "I'll help you analyze monsoon patterns and agricultural productivity in Maharashtra. Let me break this down into steps:\n\n1. First, I'll analyze the Southwest monsoon coverage and rainfall patterns across Maharashtra\n2. Then examine agricultural zones and crop distribution in the state\n3. Calculate productivity metrics for major crops like sugarcane, cotton, and soybeans\n4. Generate a visualization showing monsoon impact on agricultural yields\n\nShall I proceed with this India-specific analysis?"
    }
  ])
  const [currentMessage, setCurrentMessage] = useState('')

  const runSampleAnalysis = async () => {
    setIsLoading(true)
    try {
      const response = await fetch('/api/india/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: 'Analyze monsoon patterns and agricultural productivity in Maharashtra state'
        })
      })
      
      if (response.ok) {
        const data = await response.json()
        setAnalysisResults(data)
        
        // Add analysis steps to chat
        const newMessages = [
          ...chatMessages,
          {
            type: 'assistant',
            content: `Sample analysis completed! Completed ${data.results.length} analysis steps for: ${data.query}\n\nCheck the map for visual results and the chain-of-thought panel for detailed reasoning steps.`
          }
        ]
        setChatMessages(newMessages)
      }
    } catch (error) {
      console.error('Analysis failed:', error)
    } finally {
      setIsLoading(false)
    }
  }

  const sendMessage = async () => {
    if (!currentMessage.trim()) return
    
    const newMessages = [...chatMessages, { type: 'user', content: currentMessage }]
    setChatMessages(newMessages)
    
    setIsLoading(true)
    try {
      const response = await fetch('/api/india/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: currentMessage
        })
      })
      
      if (response.ok) {
        const data = await response.json()
        setAnalysisResults(data)
        
        setChatMessages([
          ...newMessages,
          {
            type: 'assistant',
            content: `Analysis completed for India! ${data.summary}\n\nKey findings:\n${data.results.map(r => `• ${r.explanation}`).join('\n')}`
          }
        ])
      }
    } catch (error) {
      setChatMessages([
        ...newMessages,
        {
          type: 'assistant',
          content: 'Sorry, there was an error processing your India-specific spatial analysis request.'
        }
      ])
    } finally {
      setIsLoading(false)
      setCurrentMessage('')
    }
  }

  return (
    <div className="app">
      {/* Sidebar */}
      <div className="sidebar">
        <div className="sidebar-header">
          <h2>India Spatial Analysis Agent</h2>
          <p>Chain-of-Thought GIS for India</p>
        </div>
        
        <div className="explorer">
          <h3>Explorer</h3>
          <div className="file-tree">
            <div className="folder">
              <span>📁 india_spatial_data</span>
              <div className="folder-content">
                <div className="file">📄 maharashtra_boundaries.geojson</div>
                <div className="file">📄 monsoon_data.shp</div>
                <div className="file">📄 agricultural_zones.shp</div>
              </div>
            </div>
            <div className="folder">
              <span>📁 analysis_scripts</span>
              <div className="folder-content">
                <div className="file">🐍 monsoon_analysis.py</div>
                <div className="file">🐍 crop_productivity.py</div>
                <div className="file">🐍 urban_planning_india.py</div>
              </div>
            </div>
          </div>
        </div>

        <div className="gis-tools">
          <h3>India GIS Tools</h3>
          <div className="tool">🌧️ Monsoon Analysis</div>
          <div className="tool">🌾 Agricultural Analysis</div>
          <div className="tool">🏙️ Urban Planning</div>
          <div className="tool">💨 Pollution Analysis</div>
          <div className="tool">🌊 Flood Risk Analysis</div>
          <div className="tool">👥 Demographic Analysis</div>
        </div>

        {analysisResults && (
          <div className="analysis-steps">
            <h3>Analysis Steps</h3>
            {analysisResults.results.map((result, index) => (
              <div key={index} className="step">
                <div className="step-header">
                  <span className="step-number">✓</span>
                  <span className="step-title">Step {result.step}</span>
                </div>
                <div className="step-description">
                  {result.action.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}
                </div>
                <div className="step-explanation">
                  {result.explanation}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Main Content */}
      <div className="main-content">
        <div className="tab-bar">
          <div className="tab active">
            <span>🗺️ India Spatial Analysis Map</span>
          </div>
          <div className="tab">
            <span>🐍 monsoon_analysis.py</span>
          </div>
        </div>

        <div className="editor-area">
          <div className="map-container">
            <h3>Interactive India Map View</h3>
            <p>Spatial analysis results for India will be displayed here</p>
            
            <MapComponent 
              analysisResults={analysisResults} 
              centerLat={20.5937} 
              centerLng={78.9629}
              zoom={5}
              country="India"
            />
            
            <button 
              className="run-button" 
              onClick={runSampleAnalysis}
              disabled={isLoading}
            >
              ▶ Run India Sample Analysis
            </button>

            {analysisResults && (
              <div className="map-layers">
                <h4>Map Layers</h4>
                <div className="layer">🌿 Agricultural Zones</div>
                <div className="layer">🌧️ Monsoon Patterns</div>
                <div className="layer">🏙️ Urban Centers</div>
                <div className="layer">🌊 Flood Risk Areas</div>
              </div>
            )}
          </div>
        </div>

        <div className="terminal">
          <div className="terminal-header">
            <span>▶ Terminal</span>
          </div>
          <div className="terminal-content">
            <div className="terminal-line">$ python monsoon_analysis.py</div>
            <div className="terminal-line">Loading India spatial data...</div>
            <div className="terminal-line">Processing Maharashtra state boundaries...</div>
            <div className="terminal-line">Analyzing monsoon patterns across Western Ghats...</div>
            {analysisResults && analysisResults.results.map((result, index) => (
              <div key={index} className="terminal-line">
                Step {result.step}: {result.action} - {result.explanation}
              </div>
            ))}
            {analysisResults && (
              <div className="terminal-line">Analysis complete. Results displayed on India map.</div>
            )}
            <div className="terminal-line">$</div>
          </div>
        </div>
      </div>

      {/* Chat Panel */}
      <div className="chat-panel">
        <div className="chat-header">
          <span>🤖 AI Assistant</span>
        </div>
        
        <div className="chat-messages">
          {chatMessages.map((message, index) => (
            <div key={index} className={`message ${message.type}`}>
              <div className="message-content">
                {message.content}
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="message assistant">
              <div className="message-content">
                Analyzing India spatial data...
              </div>
            </div>
          )}
        </div>

        <div className="chat-input">
          <input
            type="text"
            placeholder="Ask about India spatial analysis..."
            value={currentMessage}
            onChange={(e) => setCurrentMessage(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          />
          <button onClick={sendMessage} disabled={isLoading}>
            📤
          </button>
        </div>
      </div>
    </div>
  )
}

export default App

