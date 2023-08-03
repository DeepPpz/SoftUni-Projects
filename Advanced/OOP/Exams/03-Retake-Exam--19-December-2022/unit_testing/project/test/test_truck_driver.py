from project.truck_driver import TruckDriver
import unittest


class TruckDriverTests(unittest.TestCase):
    def setUp(self):
        self.driver = TruckDriver("Bobi", 1)
    
    def test_initialization(self):
        self.assertEqual("Bobi", self.driver.name)
        self.assertEqual(1, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
    
    def test_invalid_earned_money(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -50
        
        self.assertEqual("Bobi went bankrupt.", str(ve.exception))
    
    def test_add_cargo_offer_valid_all(self):
        result = self.driver.add_cargo_offer("Athens", 500)
        
        self.assertEqual({"Athens": 500}, self.driver.available_cargos)
        self.assertEqual("Cargo for 500 to Athens was added as an offer.", result)
    
    def test_add_cargo_offer_existing_cargo(self):
        self.driver.add_cargo_offer("Athens", 500)
        
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Athens", 500)
        
        self.assertEqual({"Athens": 500}, self.driver.available_cargos)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))
    
    def test_drive_best_cargo_offer_no_offers(self):
        result = self.driver.drive_best_cargo_offer()
        
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        self.assertEqual("There are no offers available.", result)
    
    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer("Athens", 500)
        self.driver.add_cargo_offer("Nis", 100)
        result = self.driver.drive_best_cargo_offer()
        
        self.assertEqual(460, self.driver.earned_money)
        self.assertEqual(500, self.driver.miles)
        self.assertEqual("Bobi is driving 500 to Athens.", result)
    
    def test_check_for_activities(self):
        self.driver.earned_money = 15000
        
        self.driver.check_for_activities(250)
        self.assertEqual(14980, self.driver.earned_money)
        
        self.driver.check_for_activities(1000)
        self.assertEqual(14855, self.driver.earned_money)
        
        self.driver.check_for_activities(1500)
        self.assertEqual(14190, self.driver.earned_money)
        
        self.driver.check_for_activities(10000)
        self.assertEqual(2440, self.driver.earned_money)
    
    def test_repr(self):
        self.driver.miles = 500
        result = repr(self.driver)
        expected_result = "Bobi has 500 miles behind his back."
        
        self.assertEqual(expected_result, result)
        

if __name__ == "__main__":
    unittest.main()
