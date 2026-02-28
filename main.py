import time
import numpy as np
from src.signal_processing.generator import SignalGenerator
from src.signal_processing.analyzer import SpectrumAnalyzer
from src.ai_engine.classifier import SignalClassifier
from src.ai_engine.autonomy_manager import AutonomyManager
from src.signal_processing.lpi_detector import LPIDetector
from src.jamming_logic.jammers import SmartJammer

def run_autonomous_loop():
    print("Aegis-AI Otonom EH Döngüsü Başlatılıyor...\n")
    
    sample_rate = 1e6
    duration = 0.005 # 5ms window
    
    # Initialize components
    gen = SignalGenerator(sample_rate)
    sa = SpectrumAnalyzer(sample_rate)
    classifier = SignalClassifier()
    lpi_detector = LPIDetector(sample_rate)
    jammer_map = {"Smart": SmartJammer(sample_rate)}
    autonomy = AutonomyManager(classifier, lpi_detector, jammer_map)
    
    try:
        # Loop for 5 iterations to demo
        for i in range(1, 6):
            print(f"--- [Döngü {i}] ---")
            
            # 1. EM Spektrumu Tara (Simülasyon)
            is_threat_active = (i >= 3)
            # Döngü 4'te LPI radarı simüle et
            is_lpi_radar = (i == 4)
            
            t, signal = gen.generate_noise(duration, noise_level=0.1)
            
            if is_lpi_radar:
                # FMCW Chirp (LPI)
                t_lpi = np.linspace(0, duration, int(sample_rate*duration))
                lpi_signal = np.cos(2*np.pi*(100e3*t_lpi + 50e6*t_lpi**2))
                signal = gen.add_signals(signal, lpi_signal)
                print("[ED] Spektrum Taraması: Karmaşık (LPI?) sinyal saptandı.")
            elif is_threat_active:
                target_freq = 150e3
                _, target = gen.generate_cw(target_freq, duration, amplitude=0.8)
                signal = gen.add_signals(signal, target)
                print(f"[ED] Spektrum Taraması: Sinyal saptandı ({target_freq/1e3} kHz)")
            else:
                print("[ED] Spektrum Taraması: Temiz.")

            # 2. Otonom Analiz & Karar
            freqs, mags = sa.compute_fft(signal)
            strategy = autonomy.process_detection(freqs, mags, raw_signal=signal)
            
            # 3. Müdahale Uygula
            if strategy != "None" and strategy is not None:
                print(f"[ET] Karar: MÜDAHALE GEREKLİ! Strateji: {strategy}")
                print(f"[*] SMART JAMMER DEVREDE: {strategy} uygulanıyor.")
            else:
                print("[ET] Karar: İZLEME DEVAM EDİYOR. Temiz spektrum.")
                
            print("\n")
            time.sleep(1) # Visual delay for demo
            
    except KeyboardInterrupt:
        print("\nDöngü kullanıcı tarafından durduruldu.")

if __name__ == "__main__":
    run_autonomous_loop()
