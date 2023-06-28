class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = f"{(sum(self.grades) / len(self.grades)):.2f}"
        return float(average_grade)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. " \
               f"Average grade: {Class.get_average_grade(self)}"
