from Human import Human
from typing import Literal

class Student(Human):
    def __init__(self):
        super().__init__("Student")  # Enforcing "Student" as the profession        
    
    def __set_profession(self, profession: Literal["Student"]):  # Only "Student" allowed
        """Private method in Student to prevent direct modification."""
        super().update_profession(profession)  # Calls the parent method

    def update_profession(self, new_profession: Literal["Student"]):
        """Public method to update profession using the private setter."""
        self.__set_profession(new_profession)  # Internal access only