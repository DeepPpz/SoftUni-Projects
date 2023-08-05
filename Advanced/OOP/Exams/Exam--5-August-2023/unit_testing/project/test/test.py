from project.second_hand_car import SecondHandCar
import unittest


class SecondHandCarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Golf", "Hatchback", 5000, 2000)
    
    def test_initialization(self):
        self.assertEqual("Golf", self.car.model)
        self.assertEqual("Hatchback", self.car.car_type)
        self.assertEqual(5000, self.car.mileage)
        self.assertEqual(2000, self.car.price)
        self.assertEqual([], self.car.repairs)
    
    def test_price_setter_smaller(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0
        
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_price_setter_equal(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1
        
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_mileage_setter_smaller(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 0
        
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_mileage_setter_equal(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_set_promotional_price_invalid_new_price_larger(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(5000)
        
        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_invalid_new_price_equal(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2000)
        
        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_valid_all(self):
        result = self.car.set_promotional_price(1000)
        
        self.assertEqual(1000, self.car.price)
        self.assertEqual("The promotional price has been successfully set.", result)
    
    def test_need_repair_too_expensive(self):
        result = self.car.need_repair(1500, "Turbine")
        
        self.assertEqual([], self.car.repairs)
        self.assertEqual("Repair is impossible!", result)
    
    def test_need_repair_valid_all_and_multiple(self):
        result = self.car.need_repair(500, "Turbine")
        self.assertEqual(2500, self.car.price)
        self.assertEqual(["Turbine"], self.car.repairs)
        self.assertEqual("Price has been increased due to repair charges.", result)
        
        result = self.car.need_repair(100, "Engine Mount")
        self.assertEqual(2600, self.car.price)
        self.assertEqual(["Turbine", "Engine Mount"], self.car.repairs)
        self.assertEqual("Price has been increased due to repair charges.", result)
    
    def test_gt_invalid_car_type(self):
        other_car = SecondHandCar("Eclipse", "Coupe", 5000, 8000)
        
        result = self.car.__gt__(other_car)
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test_gt_greater(self):
        other_car = SecondHandCar("Polo", "Hatchback", 5000, 1000)
        
        result = self.car.__gt__(other_car)
        self.assertTrue(result)
    
    def test_gt_lesser(self):
        other_car = SecondHandCar("Polo", "Hatchback", 5000, 3000)
        
        result = self.car.__gt__(other_car)
        self.assertFalse(result)
    
    def test_str(self):
        self.car.need_repair(500, "Turbine")
        result = str(self.car)
        expected_result = f"Model Golf | Type Hatchback | Milage 5000km\nCurrent price: 2500.00 | Number of Repairs: 1"
        
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
