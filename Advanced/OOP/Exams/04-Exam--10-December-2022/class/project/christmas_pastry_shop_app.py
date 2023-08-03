from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}
    
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0
    
    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        try:
            delicacy = next(filter(lambda x: x.name == name, self.delicacies))
            raise Exception(f"{name} already exists!")
        except StopIteration:
            pass
        
        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        
        self.delicacies.append(self.DELICACY_TYPES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."
    
    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        try:
            booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
            raise Exception(f"Booth number {booth_number} already exists!")
        except StopIteration:
            pass
        
        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")
        
        self.booths.append(self.BOOTH_TYPES[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."
    
    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception(f"No available booth for {number_of_people} people!")
    
    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")
        
        try:
            delicacy = next(filter(lambda x: x.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."
    
    def leave_booth(self, booth_number: int):
        booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        
        total_bill = booth.price_for_reservation + sum(delicacy.price for delicacy in booth.delicacy_orders)
        self.income += total_bill
        
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0
        
        return f"Booth {booth_number}:\nBill: {total_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
