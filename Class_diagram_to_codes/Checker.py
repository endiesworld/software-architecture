from PairGame import PairGame


from Human import Human

class Checkers(PairGame):
    def __init__(self, players: list[Human] = None):
        super().__init__("Checkers", players)
        
    def play(self)-> str:
        return super().play()
        