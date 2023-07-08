from typing import Union
from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms= []
        self.guests = 0
    
    @classmethod
    def from_stars(cls, stars_count: int) -> "Hotel":
        return Hotel(f"{stars_count} stars Hotel")
    
    def add_room(self, room: Room) -> None:
        self.rooms.append(room)
    
    def take_room(self, room_number, people) -> Union[str, None]:
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))
            result = room.take_room(people)
            if result is None:
                self.guests += people
        except StopIteration:
            pass
    
    def free_room(self, room_number) -> None:
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))
            self.guests -= room.guests
            room.free_room()
        except StopIteration:
            pass
    
    def status(self) -> str:
        return f"Hotel {self.name} has {self.guests} total guests\n" \
                f"Free rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken == False)}\n" \
                f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"
                