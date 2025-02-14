
from abc import ABC
from typing import Literal


class Human(ABC): # Inherits from ABC (Abstract Base Class)
    def __init__(self, profession: Literal["Student", "Teacher"]):
        self.__profession = profession # Protected attribute
    
    @property
    def profession(self) -> str:
        """Getter for profession."""
        return self.__profession
    
    def __set_profession(self, profession: Literal["Student", "Teacher"]):
        """ Setter for profession"""
        self.__profession = profession
        
    
    def update_profession(self, new_profession: Literal["Student", "Teacher"]):
        "Public method for updating the private setter for profession"
        self.__set_profession(new_profession) # Internal access only allowed.
        
    def __str__(self) -> str:
        return f"{self.__profession}"
        
        
    
    