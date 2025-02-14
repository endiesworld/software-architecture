from __future__ import annotations

from Human import Human
from PairGame import PairGame


class Client:
    
    def __init__(self):
        ...
        
        
    def main(self, player_one: Human, player_two: Human, game_one: PairGame, game_two: PairGame):
        self.player_one = player_one
        self.player_two = player_two
        
        # variable_palyer = Student() # created a variable to test that the private set_profession method is not available
        
        print("I am a :", self.player_one.profession)
        print("I am a :",self.player_two.profession)
        #print("The variable player is a: ", variable_palyer.profession)
        
        # Change the variable player profession
        """
            Any attempt to change the variable player profession by accessing the private __set_profession() method will fail
            variable_palyer.__set_profession("Teacher") 
            AttributeError: 'Student' object has no attribute '__set_profession'
        """
        # variable_palyer.update_profession("Teacher") 
        # print("The variable player is a: ", variable_palyer.profession)
        
        # Instantiating the the chess and checker games
        chess_game = game_one
        checker_game = game_two
        
        # Set player one and two for the chess game
        chess_game.player_one =self.player_two
        chess_game.player_two = self.player_one
        
        # Set player one and two for the checkers game
        checker_game.player_one =self.player_two
        checker_game.player_two = self.player_one
        
        #Prints the profession and the humans playing both games
        print(chess_game.play())
        print(checker_game.play())