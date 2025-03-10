from Human import Human
from typing import Literal

class Teacher(Human):
    def __init__(self):
        super().__init__("Teacher")  # Enforcing "Teacher" as the profession        
    
    def __set_profession(self, profession: Literal["Teacher"]):  # Only "Teacher" allowed
        """Private method in Teacher to prevent direct modification."""
        super().update_profession(profession)  # Calls the parent method

    def update_profession(self, new_profession: Literal["Teacher"]):
        """Public method to update profession using the private setter."""
        self.__set_profession(new_profession)  # Internal access only