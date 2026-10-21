students = [
    {"name": "Devang", "marks": 85},
    {"name": "Rahul", "marks": 78},
    {"name": "Priya", "marks": 92},
    {"name": "Amit", "marks": 75},
    {"name": "Ved", "marks": 65}
]

search_name = input("Enter student name: ")

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("Student Found!")
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        found = True
        break

if not found:
    print("Student not found.")