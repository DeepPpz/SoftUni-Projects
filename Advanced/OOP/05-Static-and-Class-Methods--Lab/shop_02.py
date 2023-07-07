class Shop:
    def __init__(self, name: str, type: str, capacity: int) -> None:
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
    
    @classmethod
    def small_shop(cls, name, type) -> "Shop":
        return Shop(name, type, 10)
    
    def add_item(self, item_name: str) -> str:
        if self.capacity <= sum(self.items.values()):
            return "Not enough capacity in the shop"
        else:
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f"{item_name} added to the shop"
    
    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name in self.items and amount <= self.items[item_name]:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the shop"
        else:
            return f"Cannot remove {amount} {item_name}"
    
    def __repr__(self) -> str:
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
