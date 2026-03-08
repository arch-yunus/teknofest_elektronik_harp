import numpy as np

class SignalClassifier:
    """
    AI-driven signal classification using spectrum AND pulse parameter features.
    Currently uses heuristic rule engine, designed for deep learning model plug-in.
    """
    def __init__(self):
        self.labels = ["Noise", "CW", "BPSK", "QPSK", "Pulsed_Radar", "FHSS", "LPI_Radar"]

    def extract_features(self, freqs, magnitudes):
        """
        Extracts basic spectral features from the power spectrum.
        """
        peak_idx = np.argmax(magnitudes)
        peak_freq = freqs[peak_idx]
        peak_mag = magnitudes[peak_idx]

        # Bandwidth estimation: -3 dB occupancy
        threshold = peak_mag * 0.5
        occupied_indices = np.where(magnitudes > threshold)[0]
        bandwidth = freqs[occupied_indices[-1]] - freqs[occupied_indices[0]] if len(occupied_indices) > 1 else 0

        # Spectral flatness (ratio of geometric to arithmetic mean) — detects FHSS
        eps = 1e-12
        spectral_flatness = np.exp(np.mean(np.log(magnitudes + eps))) / (np.mean(magnitudes) + eps)

        return {
            "peak_freq": peak_freq,
            "peak_mag": peak_mag,
            "bandwidth": bandwidth,
            "spectral_flatness": spectral_flatness
        }

    def predict(self, features, pulse_params=None):
        """
        Multi-feature classification with confidence score.
        Uses spectral features and optional pulse parameters.
        Returns (label, confidence).
        """
        pm = features["peak_mag"]
        bw = features["bandwidth"]
        sf = features.get("spectral_flatness", 0)

        # Pull pulse params if provided
        pri = pulse_params.get("PRI", 0) or 0 if pulse_params else 0
        pw  = pulse_params.get("PW", 0) or 0 if pulse_params else 0

        if pm < 0.15:
            return "Noise", 0.95

        # FHSS: flat spectrum + high bandwidth
        if sf > 0.6 and bw > 100e3:
            return "FHSS", 0.80

        # Pulsed radar: has PRI/PW structure
        if pulse_params and pri > 0 and pw > 0:
            duty_cycle = (pw / pri) * 100 if pri > 0 else 0
            if duty_cycle < 15:
                return "Pulsed_Radar", 0.88
            
        # Narrow CW tone
        if bw < 5000:
            return "CW", 0.90

        # BPSK / QPSK by bandwidth
        if bw < 35e3:
            return "BPSK", 0.75
        elif bw < 100e3:
            return "QPSK", 0.70

        return "Unknown", 0.50
