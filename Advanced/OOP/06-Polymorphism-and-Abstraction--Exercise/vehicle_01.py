from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, value):
        pass
    
    @abstractmethod
    def refuel(self, value):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    
    def drive(self, distance) -> None:
        fuel_needed = distance * (self.fuel_consumption + 0.9)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed
    
    def refuel(self, fuel) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    
    def drive(self, distance) -> None:
        fuel_needed = distance * (self.fuel_consumption + 1.6)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed
    
    def refuel(self, fuel) -> None:
        self.fuel_quantity += fuel * 0.95
