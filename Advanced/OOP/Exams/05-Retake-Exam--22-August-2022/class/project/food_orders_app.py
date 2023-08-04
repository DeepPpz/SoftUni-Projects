from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.main_dish import MainDish
from project.meals.dessert import Dessert
from project.client import Client


class FoodOrdersApp:
    receipt_id = 0
    
    def __init__(self):
        self.menu = []
        self.clients_list = []
    
    def register_client(self, client_phone_number: str):
        try:
            client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
            raise Exception(f"The client has already been registered!")
        except StopIteration:
            pass
        
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."
    
    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, Starter) or isinstance(meal, MainDish) or isinstance(meal, Dessert):
                self.menu.append(meal)
    
    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        
        return '\n'.join(meal.details() for meal in self.menu)
    
    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        meals_quantities = {}
        shopping_cart = []
        bill = 0.0
        
        if len(self.menu) < 5:
                raise Exception("The menu is not ready!")
        
        try:
            client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            client = Client(client_phone_number)
            self.clients_list.append(client)
        
        for meal_name, quantity in meal_names_and_quantities.items():
            try:
                meal = next(filter(lambda x: x.name == meal_name, self.menu))
            except StopIteration:
                raise Exception(f"{meal_name} is not on the menu!")
            
            if meal.quantity < quantity + meals_quantities.get(meal_name, 0):
                raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal.name}!")
            
            if meal_name not in meals_quantities:
                meals_quantities[meal_name] = 0
            
            meals_quantities[meal_name] += quantity
            shopping_cart.append(meal)
            bill += meal.price * quantity
        
        for meal_name, quantity in meals_quantities.items():
            if meal_name not in client.meals_quantities:
                client.meals_quantities[meal.name] = 0
            client.meals_quantities[meal.name] += quantity
        
        for meal_name, quantity in meals_quantities.items():
            meal = next(filter(lambda x: x.name == meal_name, self.menu))
            meal.quantity -= quantity

        client.shopping_cart.extend(shopping_cart)   
        client.bill += bill
        return f"Client {client_phone_number} successfully ordered {', '.join(x.name for x in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
        
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        
        client.shopping_cart.clear()
        client.bill = 0
        
        for meal_name, quantity in client.meals_quantities.items():
            meal = next(filter(lambda x: x.name == meal_name, self.menu))
            meal.quantity += quantity
        
        client.meals_quantities.clear()
        return f"Client {client.phone_number} successfully canceled his order."
    
    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
        
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        
        money = client.bill
        self.receipt_id += 1
        
        client.shopping_cart.clear()
        client.bill = 0
        client.meals_quantities.clear()
        
        return f"Receipt #{self.receipt_id} with total amount of {money:.2f} was successfully paid for {client_phone_number}."
    
    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
