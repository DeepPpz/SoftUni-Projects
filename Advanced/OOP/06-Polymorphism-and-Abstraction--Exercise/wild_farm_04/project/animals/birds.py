from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOOD = {"Meat"}
    weight_gain = 0.25
    
    def make_sound(self) -> str:
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOOD = {"Vegetable", "Fruit", "Meat", "Seed"}
    weight_gain = 0.35
    
    def make_sound(self) -> str:
        return "Cluck"
