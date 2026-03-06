import sys
import os
import random
import numpy as np
from flask import Flask, render_template, jsonify

# Setup path integration to access src modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.simulation.mission_engine import MissionEngine
from src.ai_engine.classifier import SignalClassifier
from src.ai_engine.autonomy_manager import AutonomyManager
from src.signal_processing.lpi_detector import LPIDetector

app = Flask(__name__)
mission_engine = MissionEngine()

# Initialize AI/EH Systems for dashboard demonstrations
classifier = SignalClassifier()
lpi_detector = LPIDetector(sample_rate=1e6)
autonomy = AutonomyManager(classifier, lpi_detector, {})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    """
    Live API bridging MissionEngine data with real-time Dashboard visualizer.
    """
    observations = mission_engine.update_environment()
    
    # Analyze the environment to formulate a real-time jamming strategy
    active_jammer = "None"
    if observations:
        # Mocking spectrum data extraction from environment for autonomy process
        freqs = np.linspace(0, 500000, 1000)
        mags = np.random.rand(1000) * 0.1
        active_jammer = autonomy.process_detection(freqs, mags)

    detected_threats = []
    for obs in observations:
        detected_threats.append({
            "type": obs["type"],
            "confidence": round(0.85 + np.random.rand() * 0.1, 2), # Example confidence simulation
            "direction": round(obs["bearing"], 1),
            "frequency": f"{obs['freq'] / 1e9:.2f} GHz"
        })

    return jsonify({
        "system_status": "Operational",
        "active_jammer": active_jammer,
        "detected_threats": detected_threats,
        "spectrum_data": (np.random.rand(100) * 0.6).tolist()
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
