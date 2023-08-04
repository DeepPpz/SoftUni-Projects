from project.computer_types.computer import Computer
import math


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}
    VALID_RAM_SIZES = [2, 4, 8, 16, 32, 64]
    
    
    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        
        if ram not in self.VALID_RAM_SIZES:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        
        processor_price = self.AVAILABLE_PROCESSORS[processor]
        ram_price = 100 * int(math.log2(ram))
        
        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price
        
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
