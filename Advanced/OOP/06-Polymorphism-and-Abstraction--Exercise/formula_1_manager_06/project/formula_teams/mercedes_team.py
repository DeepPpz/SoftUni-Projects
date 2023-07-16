from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    SPONSORS = {1: 1000000 + 100000, 2: 500000 + 100000,
                3: 500000 + 100000, 4: 100000,
                5: 100000, 6: 50000,
                7: 50000}
    EXPENSES_PER_RACE = 200000
