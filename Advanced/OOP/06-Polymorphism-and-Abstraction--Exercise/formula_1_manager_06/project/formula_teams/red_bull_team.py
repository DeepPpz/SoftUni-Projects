from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    SPONSORS = {1: 1500000 + 20000, 2: 800000 + 20000,
                3: 20000, 4: 20000,
                5: 20000, 6: 20000,
                7: 20000, 8: 20000, 
                9: 20000, 10: 10000}
    EXPENSES_PER_RACE = 250000
