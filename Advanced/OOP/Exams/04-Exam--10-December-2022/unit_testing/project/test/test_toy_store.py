from project.toy_store import ToyStore
import unittest


class ToyStoreTests(unittest.TestCase):
    def setUp(self):
        self.store = ToyStore()
    
    def test_initialization(self):
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        
        self.assertEqual(expected_result, self.store.toy_shelf)

    def test_add_toy_invalid_shelf(self):
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        
        with self.assertRaises(Exception) as ex:
            result = self.store.add_toy("Z", "Toy")
        
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual(expected_result, self.store.toy_shelf)

    def test_add_toy_existing_toy(self):
        expected_result = {
            "A": "Toy",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        
        self.store.add_toy("A", "Toy")
        
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Toy")
        
        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        self.assertEqual(expected_result, self.store.toy_shelf)
    
    def test_add_toy_filled_shelf(self):
        expected_result = {
            "A": "Toy",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        
        self.store.add_toy("A", "Toy")
        
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Game")
        
        self.assertEqual("Shelf is already taken!", str(ex.exception))
        self.assertEqual(expected_result, self.store.toy_shelf)
    
    def test_add_toy_valid_all(self):
        expected_result = {
            "A": "Toy",
            "B": "Game",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        
        result = self.store.add_toy("A", "Toy")
        self.assertEqual("Toy:Toy placed successfully!", result)
        
        result = self.store.add_toy("B", "Game")
        self.assertEqual("Toy:Game placed successfully!", result)
        self.assertEqual(expected_result, self.store.toy_shelf)
    
    def test_remove_toy_invalid_shelf(self):
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", "Toy")
                    
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual(expected_result, self.store.toy_shelf)
    
    def test_remove_toy_invalid_toy(self):
        expected_result = {
            "A": "Game",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.store.add_toy("A", "Game")
        
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Toy")
                    
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
        
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("B", "Toy")
            
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
        self.assertEqual(expected_result, self.store.toy_shelf)

    def test_remove_toy_valid_all(self):
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        
        self.store.add_toy("A", "Toy")
        self.store.add_toy("B", "Game")
        
        result = self.store.remove_toy("A", "Toy")
        self.assertEqual("Remove toy:Toy successfully!", result)
        
        result = self.store.remove_toy("B", "Game")
        self.assertEqual("Remove toy:Game successfully!", result)
        self.assertEqual(expected_result, self.store.toy_shelf)


if __name__ == '__main__':
    unittest.main()
