import unittest
from extended_list import IntegerList


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.temp_list = IntegerList(1, 2, 3.5, "test", True, 8)
    
    def test_add_operation_valid_element(self):
        self.temp_list.add(5)
        result = self.temp_list.get_data()[-1]
        self.assertEqual(5, result)
    
    def test_add_operation_invalid_element(self):        
        with self.assertRaises(ValueError) as ve:
            self.temp_list.add("test")
        
        self.assertEqual("Element is not Integer", str(ve.exception))
    
    def test_remove_index_valid_index(self):
        result = self.temp_list.remove_index(1)
        self.assertEqual(2, result)
 
    def test_remove_index_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.temp_list.remove_index(20)
        
        self.assertEqual("Index is out of range", str(ie.exception))
    
    def test_init_taking_only_integers(self):
        for el in self.temp_list.get_data():
            self.assertTrue(isinstance(el, int))
    
    def test_get_valid_index(self):
        result = self.temp_list.get(1)
        self.assertEqual(2, result)
    
    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.temp_list.get(20)
        
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_valid_all(self):
        self.temp_list.insert(1, 10)
        result = self.temp_list.get_data()[1]
        self.assertEqual(10, result)
    
    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.temp_list.insert(20, 10)
        self.assertEqual("Index is out of range", str(ie.exception))
    
    def test_insert_invalid_value(self):
        with self.assertRaises(ValueError) as ve:
            self.temp_list.insert(0, "test")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest(self):
        result = self.temp_list.get_biggest()
        self.assertEqual(8, result)
    
    def test_get_index(self):
        result = self.temp_list.get_index(1)
        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()
