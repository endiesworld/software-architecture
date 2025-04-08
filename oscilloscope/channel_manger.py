class ChannelManager:
    def __init__(self):
        self.channels = []

    def initialize_channels(self):
        self.channels = ['CH1', 'CH2', 'CH3', 'CH4']
        print("[ChannelManager] Channels initialized.")

    def assign_signal_to_channel(self, channel):
        print(f"[ChannelManager] Assigning signal to {channel}...")

    def get_raw_signal(self):
        print("[ChannelManager] Acquiring raw signal from hardware...")
        return [0.1, 0.5, -0.3, 0.6, -0.2, 0.0]  # Simulated signal