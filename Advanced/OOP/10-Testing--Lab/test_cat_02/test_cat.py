import unittest
from cat_class import Cat


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("TestCat")
        self.cat.eat()
    
    def test_increase_size(self):
        self.assertEqual(1, self.cat.size)
    
    def test_is_fed_after_eating(self):
        self.assertTrue(self.cat.fed)
    
    def test_cannot_eat_when_fed(self):        
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        
        self.assertEqual("Already fed.", str(ex.exception))
    
    def test_cannot_sleep_when_not_fed(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))
    
    def test_not_sleepy_after_sleeping(self):
        self.cat.sleep()
        
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
