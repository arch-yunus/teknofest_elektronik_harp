import numpy as np

class ScenarioManager:
    """
    Generates realistic Electronic Warfare scenarios with pulses and noise.
    """
    def __init__(self, sample_rate=1e6):
        self.sample_rate = sample_rate

    def generate_pulse_stream(self, freq, pri, pw, duration, amplitude=1.0):
        """
        Generates a stream of pulses with specified frequency, PRI, and PW.
        """
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        signal = np.zeros_like(t)
        
        num_pulses = int(duration / pri)
        for i in range(num_pulses):
            start_time = i * pri
            end_time = start_time + pw
            
            if end_time > duration:
                break
                
            start_idx = int(start_time * self.sample_rate)
            end_idx = int(end_time * self.sample_rate)
            
            # Pulse carrier
            pulse_t = t[start_idx:end_idx]
            signal[start_idx:end_idx] = amplitude * np.cos(2 * np.pi * freq * pulse_t)
            
        return t, signal

    def get_scenario_signal(self, scenario_name, duration=0.01):
        """
        Returns a signal based on predefined scenarios.
        """
        if scenario_name == "Long Range Search":
            # 150kHz frequency, 2ms PRI, 100us PW
            return self.generate_pulse_stream(150e3, 2e-3, 100e-6, duration)
        elif scenario_name == "Tracking Radar":
            # 450kHz frequency, 0.4ms PRI, 5us PW
            return self.generate_pulse_stream(450e3, 0.4e-3, 5e-6, duration)
        else:
            # Random noise
            t = np.linspace(0, duration, int(self.sample_rate * duration))
            return t, np.random.normal(0, 0.1, len(t))
