import numpy as np
from scipy.fft import fft, fftfreq

class SpectrumAnalyzer:
    """
    Performs spectral analysis on signals.
    """
    def __init__(self, sample_rate=1e6):
        self.sample_rate = sample_rate

    def compute_fft(self, signal):
        """
        Computes the Fast Fourier Transform (FFT) of the signal.
        Returns frequencies and magnitude spectrum.
        """
        N = len(signal)
        yf = fft(signal)
        xf = fftfreq(N, 1 / self.sample_rate)
        
        # Return only the positive frequencies
        return xf[:N//2], 2.0/N * np.abs(yf[0:N//2])

    def detect_peaks(self, frequencies, magnitudes, threshold=0.5):
        """
        Detects peaks in the frequency domain above a certain threshold.
        Returns a list of (frequency, magnitude) tuples.
        """
        peaks = []
        for f, m in zip(frequencies, magnitudes):
            if m > threshold:
                peaks.append((f, m))
        return peaks

class ParameterExtractor:
    """
    Extracts tactical parameters like PRI, PW, and Duty Cycle from pulses.
    """
    def __init__(self, sample_rate=1e6):
        self.sample_rate = sample_rate

    def estimate_parameters(self, time_domain_signal):
        """
        Estimates PRI (Pulse Repetition Interval), PW (Pulse Width), and Center Frequency.
        """
        # Simple threshold-based pulse detection
        threshold = np.max(np.abs(time_domain_signal)) * 0.4
        pulses = np.abs(time_domain_signal) > threshold
        
        # Find rising and falling edges
        diff = np.diff(pulses.astype(int))
        rising_edges = np.where(diff == 1)[0]
        falling_edges = np.where(diff == -1)[0]
        
        if len(rising_edges) < 1 or len(falling_edges) < 1:
            return {"PRI": None, "PW": None, "CenterFreq": None, "DutyCycle": None}
            
        # Ensure we have pairs of edges
        min_len = min(len(rising_edges), len(falling_edges))
        pws = (falling_edges[:min_len] - rising_edges[:min_len]) / self.sample_rate
        
        # Estimate Center Frequency from the first pulse (simplified)
        center_freq = 0
        if len(rising_edges) > 0:
            pulse_segment = time_domain_signal[rising_edges[0]:falling_edges[0]]
            if len(pulse_segment) > 8:
                # Use FFT on the pulse to find its dominant frequency
                N = len(pulse_segment)
                yf = fft(pulse_segment)
                xf = fftfreq(N, 1 / self.sample_rate)
                idx = np.argmax(np.abs(yf[:N//2]))
                center_freq = np.abs(xf[idx])

        pris = np.diff(rising_edges) / self.sample_rate if len(rising_edges) > 1 else [0]
        
        return {
            "PRI": np.mean(pris) if len(pris) > 0 else 0,
            "PW": np.mean(pws) if len(pws) > 0 else 0,
            "CenterFreq": center_freq,
            "DutyCycle": (np.mean(pws) / np.mean(pris)) * 100 if len(pris) > 0 and np.mean(pris) > 0 else 0
        }

class DirectionFinder:
    """
    Simulates Direction of Arrival (DoA) estimation.
    """
    def __init__(self, num_antennas=4, antenna_spacing=0.5):
        self.num_antennas = num_antennas
        self.antenna_spacing = antenna_spacing # in meters, e.g., lambda/2

    def estimate_doa_amplitude(self, signal_strengths):
        """
        Estimates the angle of arrival based on relative signal strengths (Amplitude Comparison).
        signal_strengths: list/array of magnitudes from 4 antennas (N, E, S, W)
        """
        if len(signal_strengths) != 4:
            return 0.0
            
        # Simplified ratio-based DOA
        v_diff = signal_strengths[0] - signal_strengths[2] # North - South
        h_diff = signal_strengths[1] - signal_strengths[3] # East - West
        
        angle = np.degrees(np.arctan2(h_diff, v_diff))
        return (angle + 360) % 360

    def estimate_doa_phase(self, phase_differences, wavelength):
        """
        Simulates Phase Interferometry DOA estimation for 2 antennas.
        phase_differences: phase difference in radians.
        wavelength: signal wavelength in meters.
        """
        # Phase diff = (2 * pi * d * sin(theta)) / lambda
        # sin(theta) = (Phase diff * lambda) / (2 * pi * d)
        val = (phase_differences * wavelength) / (2 * np.pi * self.antenna_spacing)
        
        # Clamp value to [-1, 1] to avoid mathematical errors
        val = max(-1.0, min(1.0, val))
        
        angle = np.degrees(np.arcsin(val))
        return angle
