
students = [
    {"name": "Devang", "marks": 85},
    {"name": "Rahul", "marks": 78},
    {"name": "Priya", "marks": 92}
]

total = 0

for student in students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])

    total = total + student["marks"]

    print("----------------")

average = total / len(students)
print("Average marks:", average)
