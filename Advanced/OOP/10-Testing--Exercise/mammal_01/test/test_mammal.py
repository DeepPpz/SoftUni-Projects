import unittest
from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Jojo", "dog", "woof")
    
    def test_initialization(self):
        self.assertEqual("Jojo", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("woof", self.mammal.sound)
    
    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Jojo makes woof", result)
    
    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)
    
    def test_info(self):
        result = self.mammal.info()
        expected_result = "Jojo is of type dog"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
