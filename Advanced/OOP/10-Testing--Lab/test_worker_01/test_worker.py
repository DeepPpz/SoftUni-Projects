import unittest
from worker_class import Worker


class WorkerTests(unittest.TestCase):
    def test_initialization(self):
        worker = Worker("Peter", 1000, 5)
        self.assertEqual("Peter", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(5, worker.energy)
        self.assertEqual(0, worker.money)
    
    def test_rest(self):
        worker = Worker("Peter", 1000, 5)
        worker.rest()
        self.assertEqual(6, worker.energy)
    
    def test_work_with_negative_energy(self):
        worker = Worker("Peter", 1000, 0)
        
        with self.assertRaises(Exception) as ex:
            worker.work()
        
        self.assertEqual("Not enough energy.", str(ex.exception))
    
    def test_work_increase_money(self):
        worker = Worker("Peter", 1000, 5)
        worker.work()
        self.assertEqual(1000, worker.money)
        
        worker.work()
        self.assertEqual(2000, worker.money)
    
    def test_work_decrease_energy(self):
        worker = Worker("Peter", 1000, 5)
        worker.work()
        self.assertEqual(4, worker.energy)
        
        worker.work()
        self.assertEqual(3, worker.energy)
    
    def test_get_info(self):
        worker = Worker("Peter", 1000, 5)
        result = worker.get_info()
        expected_result = "Peter has saved 0 money."
        self.assertEqual(expected_result, result)
        
        worker.work()
        result = worker.get_info()
        expected_result = "Peter has saved 1000 money."
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
