from project.band_members.musician import Musician


class Singer(Musician):
    AVAILABLE_TYPES = ["sing high pitch notes", "sing low pitch notes"]
    
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
