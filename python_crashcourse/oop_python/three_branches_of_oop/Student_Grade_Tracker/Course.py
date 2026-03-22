class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.enrolled_students = []

    def enroll(self, student):
        self.enrolled_students.append(student)

    def get_enrolled_students(self):
        return self.enrolled_students

    def __str__(self):
        output = self.course_name + '\n'
        for student in self.enrolled_students:
            output += str(student) + '\n'
        return output