from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Chicken(Animal):
    def make_sound(self):
        return "cluck"


animals = [Cat('Pussycat'), Dog('Doggo'), Chicken("Frank")]

for animal in animals:
    print(animal.make_sound())
