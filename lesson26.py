students = [
    {"name": "Devang", "marks": 85},
    {"name": "Rahul", "marks": 78},
    {"name": "Priya", "marks": 92},
    {"name": "Amit", "marks": 75},
    {"name": "Ved", "marks": 65}
]


def search_student(student_list, search_name):
    for student in student_list:
        if student["name"].lower() == search_name.lower():
            return student

    return None


name = input("Enter student name: ")

result = search_student(students, name)

if result is not None:
    print("Student Found!")
    print("Name:", result["name"])
    print("Marks:", result["marks"])
else:
    print("Student not found.")