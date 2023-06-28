class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        circumference = Circle.__pi * self.diameter
        return circumference

    def calculate_area(self):
        area = Circle.__pi * self.radius ** 2
        return area

    def calculate_area_of_sector(self, angle):
        sector_area = (angle / 360) * Circle.__pi * self.radius ** 2
        return sector_area
