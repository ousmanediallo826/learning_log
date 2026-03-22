from Student import Student
from Course import Course
from GradeBook import GradeBook

# --- Setup ---
gb = GradeBook()
gb.load_data()  # loads from file if it exists

# --- Create Students ---
s1 = Student('Alice')
s2 = Student('Bob')
s3 = Student('Charlie')

# --- Create Courses ---
c1 = Course('Math')
c2 = Course('Python 101')

# --- Add to GradeBook ---
gb.add_student(s1)
gb.add_student(s2)
gb.add_student(s3)

gb.add_course(c1)
gb.add_course(c2)

# --- Enroll Students ---
gb.enroll_student(s1, c1)
gb.enroll_student(s1, c2)
gb.enroll_student(s2, c1)
gb.enroll_student(s3, c2)

# --- Assign Grades ---
gb.assign_grade(s1, c1, 90)
gb.assign_grade(s1, c2, 85)
gb.assign_grade(s2, c1, 78)
gb.assign_grade(s3, c2, 92)

# --- Display All ---
print('\n--- All Students ---')
gb.display_all()

# --- Save ---
gb.save_data()

print('\nDone. Run the file again to confirm load_data works.')