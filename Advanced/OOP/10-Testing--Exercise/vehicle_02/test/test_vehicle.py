import unittest
from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 90)
    
    def test_initialization(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(90, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
    
    def test_drive_valid_all(self):
        self.vehicle.drive(20)
        
        self.assertEqual(25, self.vehicle.fuel)
    
    def test_drive_invalid_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))
    
    def test_refuel_valid_all(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(20)
        
        self.assertEqual(45, self.vehicle.fuel)
    
    def test_fuel_invalid_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(ex.exception))
    
    def test_str(self):
        result = str(self.vehicle)
        
        self.assertEqual("The vehicle has 90 horse power with 50 fuel left and 1.25 fuel consumption", result)


if __name__ == "__main__":
    unittest.main()
