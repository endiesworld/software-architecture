from PairGame import PairGame


from Human import Human

class Chess(PairGame):
    def __init__(self, players: list[Human] = None):
        super().__init__("Chess", players)
        
    def play(self)-> str:
        return super().play()
        