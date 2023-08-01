import unittest
from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Pesho", 5, 100, 20)
    
    def test_initialization(self):
        self.assertEqual("Pesho", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(20, self.hero.damage)
    
    def test_battle_same_username(self):
        enemy_hero = Hero("Pesho", 5, 100, 20)
        
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        
        self.assertEqual("You cannot fight yourself", str(ex.exception))
    
    def test_battle_low_player_health(self):
        enemy_hero = Hero("Gosho", 5, 100, 20)
        self.hero.health = -5
        
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)
        
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))
    
    def test_battle_low_enemy_health(self):
        enemy_hero = Hero("Gosho", 5, -5, 20)
        
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)
        
        self.assertEqual("You cannot fight Gosho. He needs to rest", str(ve.exception))

    def test_battle_draw_case(self):
        enemy_hero = Hero("Gosho", 5, 100, 20)
        result = self.hero.battle(enemy_hero)
        
        self.assertEqual("Draw", result)
    
    def test_battle_win_case(self):
        enemy_hero = Hero("Gosho", 5, 100, 10)
        result = self.hero.battle(enemy_hero)
        
        self.assertEqual("You win", result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(25, self.hero.damage)
    
    def test_battle_lose_case(self):
        self.hero.damage = 10
        enemy_hero = Hero("Gosho", 5, 100, 20)
        result = self.hero.battle(enemy_hero)
        
        self.assertEqual("You lose", result)
        self.assertEqual(6, enemy_hero.level)
        self.assertEqual(55, enemy_hero.health)
        self.assertEqual(25, enemy_hero.damage)

    def test_str(self):
        result = str(self.hero)
        
        self.assertEqual("Hero Pesho: 5 lvl\nHealth: 100\nDamage: 20\n", result)


if __name__ == "__main__":
    unittest.main()
