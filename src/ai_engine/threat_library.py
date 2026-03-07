class ThreatLibrary:
    """
    Database of known threat signatures and their characteristics.
    """
    THREATS = {
        "Long Range Radar": {
            "label": "Radar_L",
            "freq_range": (100e3, 200e3), # Adjusted for sim consistency
            "pri_range": (1e-3, 3e-3),
            "pw_range": (50e-6, 500e-6),
            "countermeasure": "NoiseJamming"
        },
        "Fire Control Radar": {
            "label": "Radar_FC",
            "freq_range": (400e3, 500e3),
            "pri_range": (0.1e-3, 0.5e-3),
            "pw_range": (1e-6, 10e-6),
            "countermeasure": "Spoofing"
        },
        "Tactical Data Link": {
            "label": "Comm_Link",
            "freq_range": (200e3, 400e3),
            "modulation": "QPSK",
            "countermeasure": "SmartJamming"
        }
    }

    @staticmethod
    def identify_emitter(params):
        """
        Identifies the emitter by matching parameters against the library.
        """
        freq = params.get("CenterFreq", 0)
        pri = params.get("PRI", 0)
        pw = params.get("PW", 0)

        for name, data in ThreatLibrary.THREATS.items():
            f_min, f_max = data.get("freq_range", (0, 0))
            p_min, p_max = data.get("pri_range", (0, 0))
            pw_min, pw_max = data.get("pw_range", (0, 0))

            # Fuzzy match (within ranges or close to them)
            freq_match = (f_min <= freq <= f_max) if f_max > 0 else True
            pri_match = (p_min * 0.8 <= pri <= p_max * 1.2) if p_max > 0 else True
            # PW is often more variable in simulation
            pw_match = (pw_min * 0.5 <= pw <= pw_max * 2.0) if pw_max > 0 else True

            if freq_match and pri_match and pw_match:
                return name, data
        
        return "Unknown", {"label": "Unknown", "countermeasure": "NoiseJamming"}

    @staticmethod
    def get_countermeasure(label):
        for threat, data in ThreatLibrary.THREATS.items():
            if data["label"] == label:
                return data["countermeasure"]
        return "NoiseJamming" # Default
