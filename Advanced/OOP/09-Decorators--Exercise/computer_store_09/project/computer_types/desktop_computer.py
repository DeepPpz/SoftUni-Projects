from project.computer_types.computer import Computer
import math


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
    VALID_RAM_SIZES = [2, 4, 8, 16, 32, 64, 128]
    
    
    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        
        if ram not in self.VALID_RAM_SIZES:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        
        processor_price = self.AVAILABLE_PROCESSORS[processor]
        ram_price = 100 * int(math.log2(ram))
        
        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price
        
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
