from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOOD = {"Vegetable", "Fruit"}
    weight_gain = 0.10
    
    def make_sound(self) -> str:
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOOD = {"Meat"}
    weight_gain = 0.40
    
    def make_sound(self) -> str:
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOOD = {"Vegetable", "Meat"}
    weight_gain = 0.30
    
    def make_sound(self) -> str:
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOOD = {"Meat"}
    weight_gain = 1.00
    
    def make_sound(self) -> str:
        return "ROAR!!!"
