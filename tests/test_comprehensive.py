import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from jamming_logic.jammers import JammerCoordinator, AdaptiveNoiseJammer
from ai_engine.autonomy_manager import AutonomyManager
from signal_processing.lpi_detector import LPIDetector
from ai_engine.classifier import SignalClassifier

def test_jammer_coordinator():
    coord = JammerCoordinator(1e6)
    coord.assign_jammer("T1", "LPI_Radar", 9)
    coord.assign_jammer("T2", "FHSS", 7)
    
    t, sig = coord.generate_combined_signal(0.001)
    assert len(sig) > 0
    assert len(coord.active_assignments) == 2

def test_adaptive_jammer_boost():
    jammer = AdaptiveNoiseJammer(1e6)
    jammer.set_power(20)
    # Risk 10 should boost power
    t, sig_high = jammer.generate_jamming_signal(0.001, threat_risk=10)
    
    # Risk 3 should not boost power (boost = max(0, (3-5)*2) = 0)
    t, sig_low = jammer.generate_jamming_signal(0.001, threat_risk=3)
    
    assert np.std(sig_high) > np.std(sig_low)

def test_autonomy_priority():
    clf = SignalClassifier()
    lpi = LPIDetector(1e6)
    mgr = AutonomyManager(clf, lpi, {})
    
    # Simulate high risk threat
    mgr.threat_log.append({"threat": "LPI", "label": "LPI_Radar", "risk": 9, "confidence": 0.9})
    # Simulate low risk threat
    mgr.threat_log.append({"threat": "Comm", "label": "Comm_Link", "risk": 4, "confidence": 0.8})
    
    top = mgr.get_highest_priority_threat()
    assert top["label"] == "LPI_Radar"

if __name__ == "__main__":
    pytest.main([__file__])
