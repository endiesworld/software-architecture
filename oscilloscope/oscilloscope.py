from channel_manger import ChannelManager
from interaction_controller import InteractionController
from signal_analyzer import PeakDetector
from signal_processor import SignalOffset
from interaction_controller import InteractionController

if __name__ == "__main__":
    cm = ChannelManager()
    cm.initialize_channels()

    processor = SignalOffset()
    analyzer = PeakDetector()
    controller = InteractionController(cm, processor, analyzer)

    controller.handle_user_input("zoom")
    controller.handle_user_input("style")
    controller.handle_user_input("signal")
    controller.handle_user_input("analyze")