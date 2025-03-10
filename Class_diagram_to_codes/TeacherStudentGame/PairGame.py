from abc import ABC
from typing import Literal

from Human import Human


class PairGame(ABC):
    
    def __init__(self, game: Literal["Chess", "Checkers"], players: list[Human] = None):
        self.__game = game
        self.__m_players = players if players else [None, None]
        
    @property
    def game(self):
        """Getter for the game"""
        return self.__game
        
    @property
    def player_one(self)-> Human:
        """Getter for player one."""
        return self.__m_players[0]
    
    @property
    def player_two(self)-> Human:
        """Getter for player two."""
        return self.__m_players[1]
        
    @player_one.setter
    def player_one(self, player: Human):
        if not isinstance(player, Human):
            raise ValueError("Player must be approved Human object")
        self.__m_players[0] = player
        
    @player_two.setter
    def player_two(self, player: Human):
        if not isinstance(player, Human):
            raise ValueError("Player must be approved Human object")
        # Prevents setting second player if first player is not set
        if not self.__m_players[0]:
            raise ValueError("Enter player one first")
        self.__m_players[1] = player
    
    
    def play(self)-> str:
        return f"The profession for player one is {self.player_one}, while the profession for player two is {self.player_two}, and they are both playing {self.game}."
        
    
    def __str__(self)-> str:
        return f"The profession for player one is {self.player_one}, while the profession for player two is {self.player_two}, and they are both playing {self.game}."