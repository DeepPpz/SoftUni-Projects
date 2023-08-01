import unittest
from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.student_without_courses = Student("Gosho")
        self.default_student = Student("Pesho", {"Python": ["very hard"]})
    
    def test_initialization(self):
        self.assertEqual("Gosho", self.student_without_courses.name)
        self.assertEqual({}, self.student_without_courses.courses)
        self.assertEqual("Pesho", self.default_student.name)
        self.assertEqual({"Python": ["very hard"]}, self.default_student.courses)
    
    def test_enroll_existing_course(self):
        result = self.default_student.enroll("Python", ["can't stop"])
        
        self.assertEqual(["very hard", "can't stop"], self.default_student.courses["Python"])
        self.assertEqual("Course already added. Notes have been updated.", result)
    
    def test_enroll_new_course_with_add_notes_y_or_null(self):
        result = self.default_student.enroll("PostgreSQL", ["very fun"], "Y")
        
        self.assertEqual(2, len(self.default_student.courses))
        self.assertEqual(["very fun"], self.default_student.courses["PostgreSQL"])
        self.assertEqual("Course and course notes have been added.", result)
        
        result = self.default_student.enroll("HTML", ["hate front-end"])
        
        self.assertEqual(3, len(self.default_student.courses))
        self.assertEqual(["hate front-end"], self.default_student.courses["HTML"])
        self.assertEqual("Course and course notes have been added.", result)
    
    def test_enroll_new_course_with_add_notes_else(self):
        result = self.default_student.enroll("PostgreSQL", ["very fun"], "N")
        
        self.assertEqual(2, len(self.default_student.courses))
        self.assertEqual([], self.default_student.courses["PostgreSQL"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_existing_course(self):
        result = self.default_student.add_notes("Python", "can't stop")
        
        self.assertEqual(["very hard", "can't stop"], self.default_student.courses["Python"])
        self.assertEqual("Notes have been updated", result)
    
    def test_add_notes_invalid_course(self):
        with self.assertRaises(Exception) as ex:
            self.default_student.add_notes("PostgreSQL", "very fun")
        
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
    
    def test_leave_course_existing_course(self):
        result = self.default_student.leave_course("Python")
        
        self.assertEqual(0, len(self.default_student.courses))
        self.assertEqual("Course has been removed", result)
    
    def test_leave_course_invalid_course(self):
        with self.assertRaises(Exception) as ex:
            self.default_student.leave_course("PostgreSQL")
        
        self.assertEqual(1, len(self.default_student.courses))
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
