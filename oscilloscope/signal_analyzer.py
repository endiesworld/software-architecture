from abc import ABC, abstractmethod

class SignalAnalyzer(ABC):
    @abstractmethod
    def analyze_frequency(self):
        pass

    @abstractmethod
    def compute_peak_to_peak(self):
        pass
    
    

class PeakDetector(SignalAnalyzer):
    def __init__(self):
        self.signal = []

    def analyze_frequency(self):
        print("[PeakDetector] Analyzing signal in frequency domain...")

    def compute_peak_to_peak(self):
        print("[PeakDetector] Computing peak-to-peak value...")
        if self.signal:
            p2p = max(self.signal) - min(self.signal)
            print(f"[PeakDetector] Peak-to-Peak: {p2p}")
        else:
            print("[PeakDetector] No signal to analyze.")