from abc import ABC


class FormulaTeam(ABC):
    SPONSORS = {}
    EXPENSES_PER_RACE = 0
    
    def __init__(self, budget: int) -> None:
        self.budget = budget
    
    @property
    def budget(self) -> int:
        return self.__budget
    
    @budget.setter
    def budget(self, value) -> None:
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        
        self.__budget = value
    
    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = self.SPONSORS.get(race_pos, 0) - self.EXPENSES_PER_RACE
        self.budget += revenue
        
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
    