import unittest
from car_manager import Car


class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("Volkswagen", "Golf 4", 5, 55)
    
    def test_initialization_valid_values(self):
        self.assertEqual("Volkswagen", self.car.make)
        self.assertEqual("Golf 4", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(55, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)
    
    def test_initialization_invalid_make(self):
        with self.assertRaises(Exception) as ex:
            Car("", "Golf 4", 5, 55)
        
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
    
    def test_initialization_invalid_model(self):
        with self.assertRaises(Exception) as ex:
            Car("Volkswagen", "", 5, 55)
        
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_initialization_invalid_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            Car("Volkswagen", "Golf 4", 0, 55)
        
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_initialization_invalid_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            Car("Volkswagen", "Golf 4", 5, 0)
        
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_assignment_fuel_amount(self):
        self.car.fuel_amount = 50
        
        self.assertEqual(50, self.car.fuel_amount)
    
    def test_assignment_fuel_amount_invalid_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = - 50
        
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_valid_fuel(self):
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)
        
        self.car.refuel(30)
        self.assertEqual(50, self.car.fuel_amount)
        
        self.car.refuel(20)
        self.assertEqual(55, self.car.fuel_amount)
    
    def test_refuel_invalid_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-20)
        
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
    
    def test_drive_valid_distance(self):
        self.car.refuel(55)
        self.car.drive(100)
        
        self.assertEqual(50, self.car.fuel_amount)
    
    def test_drive_invalid_all(self):        
        with self.assertRaises(Exception) as ex:
            self.car.drive(5)
        
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
