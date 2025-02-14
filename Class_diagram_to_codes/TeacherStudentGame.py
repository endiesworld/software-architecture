
from Client import Client
from Student import Student
from Teacher import Teacher
from Checker import Checkers
from Chess import Chess
        

if __name__ == '__main__':
    player_one = Teacher()
    player_two = Student()
    
    chess_game = Chess()
    checker_game = Checkers()
    
    client = Client()
    client.main(player_one, player_two, chess_game, checker_game)