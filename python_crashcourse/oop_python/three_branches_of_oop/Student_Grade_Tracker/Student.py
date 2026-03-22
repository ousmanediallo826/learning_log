class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = {}

    def add_grade(self, course, grade):
        self.__grades[course] = grade

    def get_grade(self, course):
        return self.__grades.get(course, 'No grade found')

    def get_gpa(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def __str__(self):
        return f'{self.name} | GPA: {self.get_gpa():.2f}'

    def get_grades(self):
        return self.__grades