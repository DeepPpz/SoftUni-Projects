from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []
    
    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        
        try:
            musician = next(filter(lambda x: x.name == name, self.musicians))
            raise Exception(f"{name} is already a musician!")
        except StopIteration:
            pass
        
        self.musicians.append(self.VALID_MUSICIAN_TYPES[musician_type](name, age))
        return f"{name} is now a {musician_type}."
    
    def create_band(self, name: str):
        try:
            band = next(filter(lambda x: x.name == name, self.bands))
            raise Exception(f"{name} band is already created!")
        except StopIteration:
            pass
        
        self.bands.append(Band(name))
        return f"{name} was created."
    
    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            concert = next(filter(lambda x: x.place == place, self.concerts))
            raise Exception(f"{place} is already registered for {concert.genre} concert!")
        except StopIteration:
            pass
        
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."
    
    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = next(filter(lambda x: x.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")
        
        try:
            band = next(filter(lambda x: x.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")
        
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."
    
    def remove_musician_from_band(self, musician_name: str, band_name: str):        
        try:
            band = next(filter(lambda x: x.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")
        
        try:
            musician = next(filter(lambda x: x.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."
    
    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda x: x.name == band_name, self.bands))
        concert = next(filter(lambda x: x.place == concert_place, self.concerts))
        
        if not any(x for x in band.members if type(x).__name__ == "Singer") or \
            not any(x for x in band.members if type(x).__name__ == "Drummer") or \
                not any(x for x in band.members if type(x).__name__ == "Guitarist"):
                    raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")
        
        if concert.genre == "Rock":
            if not any([x for x in mem.skills if x == "play the drums with drumsticks"] for mem in band.members if type(mem).__name__ == "Drummer") or \
                not any([x for x in mem.skills if x == "sing high pitch notes"] for mem in band.members if type(mem).__name__ == "Singer") or \
                    not any([x for x in mem.skills if x == "play rock"] for mem in band.members if type(mem).__name__ == "Guitarist"):
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
        elif concert.genre == "Metal":
            if not any([x for x in mem.skills if x == "play the drums with drumsticks"] for mem in band.members if type(mem).__name__ == "Drummer") or \
                not any([x for x in mem.skills if x == "sing low pitch notes"] for mem in band.members if type(mem).__name__ == "Singer") or \
                    not any([x for x in mem.skills if x == "play metal"] for mem in band.members if type(mem).__name__ == "Guitarist"):
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
        elif concert.genre == "Jazz":
            if not any([x for x in mem.skills if x == "play the drums with drum brushes"] for mem in band.members if type(mem).__name__ == "Drummer") or \
                not any([x for x in mem.skills if x == "sing high pitch notes"] for mem in band.members if type(mem).__name__ == "Singer") or \
                    not any([x for x in mem.skills if x == "sing low pitch notes"] for mem in band.members if type(mem).__name__ == "Singer") or \
                        not any([x for x in mem.skills if x == "play jazz"] for mem in band.members if type(mem).__name__ == "Guitarist"):
                            raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
