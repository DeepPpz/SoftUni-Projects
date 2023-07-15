from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self) -> str:
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"
    
    @abstractmethod
    def make_sound(self):
        pass