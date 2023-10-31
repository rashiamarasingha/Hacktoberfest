
grading_scale = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0
}

total_grade_points = 0
total_credit_hours = 0


num_courses = int(input("Enter the number of courses: "))


for i in range(num_courses):
    course_grade = input(f"Enter the grade for course {i + 1}: ").upper()
    credit_hours = float(input(f"Enter the credit hours for course {i + 1}: "))
    
    
    if course_grade in grading_scale:
        grade_points = grading_scale[course_grade]
        total_grade_points += grade_points * credit_hours
        total_credit_hours += credit_hours
    else:
        print(f"Invalid grade entered for course {i + 1}. Skipping this course.")


if total_credit_hours > 0:
    gpa = total_grade_points / total_credit_hours
    print(f"Your GPA is: {gpa:.2f}")
else:
    print("No valid courses entered for GPA calculation.")

