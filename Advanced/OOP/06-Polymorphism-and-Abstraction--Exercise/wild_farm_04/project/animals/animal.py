from abc import ABC, abstractmethod
from typing import Union
from project.food import Food


class Animal(ABC):
    ALLOWED_FOOD = set()
    weight_gain = 0.0
    
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = 0
    
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def feed(self, value):
        pass


class Bird(Animal, ABC):    
    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size
    
    def feed(self, food: Food) -> Union[str, None]:
        food_type = type(food).__name__
        if food_type not in self.ALLOWED_FOOD:
            return f"{type(self).__name__} does not eat {food_type}!"
        
        self.food_eaten += food.quantity
        self.weight += self.weight_gain * food.quantity
    
    def __repr__(self) -> str:
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):    
    def __init__(self, name: str, weight: float, living_region: str) -> None:
        super().__init__(name, weight)
        self.living_region = living_region
    
    def feed(self, food: Food) -> Union[str, None]:
        food_type = type(food).__name__
        if food_type not in self.ALLOWED_FOOD:
            return f"{type(self).__name__} does not eat {food_type}!"
        
        self.food_eaten += food.quantity
        self.weight += self.weight_gain * food.quantity
    
    def __repr__(self) -> str:
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
