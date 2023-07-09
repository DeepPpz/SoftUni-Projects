from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.__radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height: int, width: int) -> None:
        self.__height = height
        self.__width = width

    def calculate_area(self) -> int:
        return self.__height * self.__width

    def calculate_perimeter(self) -> int:
        return 2 * (self.__height + self.__width)
