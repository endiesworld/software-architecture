from abc import ABC, abstractmethod


# ---------- INTERFACES ----------
class SignalProcessor(ABC):
    @abstractmethod
    def process_signal(self, signal):
        pass


# ---------- IMPLEMENTATIONS ----------
class SignalOffset(SignalProcessor):
    def process_signal(self, signal):
        print("[SignalOffset] Applying vertical offset to signal...")
        return [x + 0.5 for x in signal]  # Simulated offset
