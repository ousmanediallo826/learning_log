import json
import os
from Student import *
from Course import *


class GradeBook:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student):
        self.students[student.name] = student
        print('Student added successfully.')

    def add_course(self, course):
        self.courses[course.course_name] = course
        print('Course added successfully.')

    def enroll_student(self, student, course):
        if student.name in self.students and course.course_name in self.courses:
            self.courses[course.course_name].enroll(student)
            print(f'{student.name} has been enrolled in {course.course_name}.')
        else:
            print('Student or course not found. Make sure to add them first.')

    def assign_grade(self, student, course, grade):
        if student.name in self.students:
            self.students[student.name].add_grade(course.course_name, grade)
            print(f'Grade of {grade} assigned to {student.name} for {course.course_name}.')
        else:
            print(f'Student {student.name} not found.')

    def display_all(self):
        if not self.students:
            print('No students found.')
            return
        for student in self.students.values():
            print(f'\nStudent: {student.name}')
            grades = student.get_grades()
            if grades:
                for course, grade in grades.items():
                    print(f'  {course}: {grade}')
            else:
                print('  No grades assigned yet.')
            print(f'  GPA: {student.get_gpa():.2f}')

    def save_data(self):
        data = {
            'students': {},
            'courses': {}
        }
        for name, student in self.students.items():
            data['students'][name] = {
                'name': student.name,
                'grades': student.get_grades()
            }
        for course_name, course in self.courses.items():
            data['courses'][course_name] = {
                'course_name': course.course_name,
                'enrolled_students': [s.name for s in course.get_enrolled_students()]
            }
        os.makedirs('data', exist_ok=True)
        with open('data/grades.json', 'w') as f:
            json.dump(data, f, indent=4)
        print('Data saved successfully.')

    def load_data(self):
        if not os.path.exists('data/grades.json'):
            print('No saved data found. Starting fresh.')
            return
        with open('data/grades.json', 'r') as f:
            data = json.load(f)
        for name, student_data in data['students'].items():
            student = Student(student_data['name'])
            for course, grade in student_data['grades'].items():
                student.add_grade(course, grade)
            self.students[name] = student
        for course_name, course_data in data['courses'].items():
            course = Course(course_data['course_name'])
            for student_name in course_data['enrolled_students']:
                if student_name in self.students:
                    course.enroll(self.students[student_name])
            self.courses[course_name] = course
        print('Data loaded successfully.')