from project.robot import Robot
import unittest


class RobotTest(unittest.TestCase):
    def setUp(self) -> None:
        self.robot = Robot("R2-D2", "Military", 50, 1)
    
    def test_initialization_valid_values(self):
        self.assertEqual("R2-D2", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(50, self.robot.available_capacity)
        self.assertEqual(1, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)
    
    def test_initialization_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            Robot("R2-D2", "B", 50, 1)
        
        self.assertEqual(f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ve.exception))
    
    def test_initialization_invalid_price(self):
        with self.assertRaises(ValueError) as ve:
            Robot("R2-D2", "Military", 50, -5)
        
        self.assertEqual("Price cannot be negative!", str(ve.exception))
    
    def test_upgrade_valid_all(self):
        result = self.robot.upgrade("h", 5)
        
        self.assertEqual(["h"], self.robot.hardware_upgrades)
        self.assertEqual(8.5, self.robot.price)
        self.assertEqual("Robot R2-D2 was upgraded with h.", result)
    
    def test_upgrade_existing_hardware(self):
        result = self.robot.upgrade("h", 5)
        result = self.robot.upgrade("h", 5)
        
        self.assertEqual(["h"], self.robot.hardware_upgrades)
        self.assertEqual(8.5, self.robot.price)
        self.assertEqual("Robot R2-D2 was not upgraded.", result)
    
    def test_upgrade_add_multiple(self):
        result = self.robot.upgrade("h", 5)
        result = self.robot.upgrade("h1", 5)
        
        self.assertEqual(["h", "h1"], self.robot.hardware_upgrades)
        self.assertEqual(16, self.robot.price)
        self.assertEqual("Robot R2-D2 was upgraded with h1.", result)
    
    def test_update_valid_all(self):
        result = self.robot.update(1.1, 10)
        
        self.assertEqual([1.1], self.robot.software_updates)
        self.assertEqual(40, self.robot.available_capacity)
        self.assertEqual("Robot R2-D2 was updated to version 1.1.", result)
    
    def test_update_add_multiple(self):
        result = self.robot.update(1.1, 10)
        result = self.robot.update(1.2, 10)
        
        self.assertEqual([1.1, 1.2], self.robot.software_updates)
        self.assertEqual(30, self.robot.available_capacity)
        self.assertEqual("Robot R2-D2 was updated to version 1.2.", result)
    
    def test_update_old_version(self):
        result = self.robot.update(1.9, 10)
        result = self.robot.update(1.1, 10)
        
        self.assertEqual([1.9], self.robot.software_updates)
        self.assertEqual(40, self.robot.available_capacity)
        self.assertEqual("Robot R2-D2 was not updated.", result)
    
    def test_update_same_version(self):
        result = self.robot.update(1.9, 10)
        result = self.robot.update(1.9, 10)
        
        self.assertEqual([1.9], self.robot.software_updates)
        self.assertEqual(40, self.robot.available_capacity)
        self.assertEqual("Robot R2-D2 was not updated.", result)
    
    def test_update_invalid_capacity(self):
        result = self.robot.update(1.9, 100)
        
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(50, self.robot.available_capacity)
        self.assertEqual("Robot R2-D2 was not updated.", result)
    
    def test_gt_greater(self):
        robot_two = Robot("Emo", "Entertainment", 20, 0.5)
        result = self.robot > robot_two
        self.assertEqual("Robot with ID R2-D2 is more expensive than Robot with ID Emo.", result)

    def test_gt_less(self):
        robot_two = Robot("Emo", "Entertainment", 20, 1.5)
        result = robot_two < self.robot
        self.assertEqual("Robot with ID R2-D2 is cheaper than Robot with ID Emo.", result)

    def test_gt_equal(self):
        robot_two = Robot("Emo", "Entertainment", 20, 1)
        result = self.robot.__gt__(robot_two)
        self.assertEqual("Robot with ID R2-D2 costs equal to Robot with ID Emo.", result)
        

if __name__ == "__main__":
    unittest.main()
