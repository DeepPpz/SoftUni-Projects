import re


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0
        self.meals_quantities = {}
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        pattern = r'^0\d{9}$'
        if not re.match(pattern, value):
            raise ValueError("Invalid phone number!")
        
        self.__phone_number = value
