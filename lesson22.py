
students = [
    {"name": "Devang", "marks": 85},
    {"name": "Rahul", "marks": 78},
    {"name": "Priya", "marks": 92},
    {"name": "Amit", "marks": 75},
    {"name": "Ved", "marks": 65},
]

for student in students:
    marks = student["marks"]

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "D"

    print(student["name"], "-", marks, "-", grade)
