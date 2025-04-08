from channel_manger import ChannelManager
from signal_analyzer import SignalAnalyzer
from signal_processor import SignalProcessor
from display_manager import DisplayManager


class InteractionController:
    def __init__(self, 
                 channel_manager: ChannelManager,
                 processor: SignalProcessor,
                 analyzer: SignalAnalyzer):
        self.channel_manager = channel_manager
        self.signal_processor = processor
        self.signal_analyzer = analyzer
        self.display_manager = DisplayManager()

    def handle_user_input(self, input_type):
        print(f"[InteractionController] Handling user input: {input_type}")

        if input_type == "zoom":
            self.display_manager.apply_zoom()

        elif input_type == "style":
            self.display_manager.set_channel_style("CH1", "blue")

        elif input_type == "signal":
            raw = self.channel_manager.get_raw_signal()
            processed = self.signal_processor.process_signal(raw)
            self.signal_analyzer.signal = processed

        elif input_type == "analyze":
            self.signal_analyzer.compute_peak_to_peak()