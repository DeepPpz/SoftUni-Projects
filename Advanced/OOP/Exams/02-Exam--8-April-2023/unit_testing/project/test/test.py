from project.tennis_player import TennisPlayer
import unittest


class TennisPlayerTests(unittest.TestCase):
    def setUp(self):
        self.player = TennisPlayer("Pesho", 33, 10.5)
    
    def test_initialization(self):
        self.assertEqual("Pesho", self.player.name)
        self.assertEqual(33, self.player.age)
        self.assertEqual(10.5, self.player.points)
        self.assertEqual([], self.player.wins)
    
    def test_invalid_name_one_symbol(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("P", 33, 10.5)
        
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))
    
    def test_invalid_name_two_symbols(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("Pe", 33, 10.5)
        
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))
    
    def test_invalid_age(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("Pesho", 3, 10.5)
        
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_new_tournaments(self):
        self.player.add_new_win("The Championships")
        self.assertEqual(["The Championships"], self.player.wins)
        
        self.player.add_new_win("The Championships v2")
        self.assertEqual(["The Championships", "The Championships v2"], self.player.wins)
    
    def test_add_new_win_existing_tournament(self):
        self.player.add_new_win("The Championships")
        result = self.player.add_new_win("The Championships")
        
        self.assertEqual(["The Championships"], self.player.wins)
        self.assertEqual("The Championships has been already added to the list of wins!", result)
    
    def test_lt_less(self):
        player_two = TennisPlayer("Gosho", 30, 20.5)
        result = self.player.__lt__(player_two)
        
        self.assertEqual("Gosho is a top seeded player and he/she is better than Pesho", result)
    
    def test_lt_greater(self):
        player_two = TennisPlayer("Gosho", 30, 5.5)
        result = self.player.__lt__(player_two)
        
        self.assertEqual("Pesho is a better player than Gosho", result)
    
    def test_str_with_wins(self):
        self.player.add_new_win("The Championships")
        self.player.add_new_win("The Championships v2")
        result = str(self.player)
        expected_result = "Tennis Player: Pesho\nAge: 33\nPoints: 10.5\nTournaments won: The Championships, The Championships v2"
        
        self.assertEqual(expected_result, result)
    
    def test_str_without_wins(self):
        result = str(self.player)
        expected_result = "Tennis Player: Pesho\nAge: 33\nPoints: 10.5\nTournaments won: "
        
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
