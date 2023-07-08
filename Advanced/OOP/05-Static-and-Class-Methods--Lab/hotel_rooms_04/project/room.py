from typing import Union


class Room:
    def __init__(self, number: int, capacity: int) -> None:
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False
        
    def take_room(self, people) -> Union[str, None]:
        if not self.is_taken and self.capacity >= people:
            self.guests = people
            self.is_taken = True
        else:
            return f"Room number {self.number} cannot be taken"

    def free_room(self) -> Union[str, None]:
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
        else:
            return f"Room number {self.number} is not taken"
