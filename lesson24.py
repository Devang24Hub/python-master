students = [
    {"name": "Devang", "marks": 85},
    {"name": "Rahul", "marks": 78},
    {"name": "Priya", "marks": 92},
    {"name": "Amit", "marks": 75},
    {"name": "Ved", "marks": 65}
]

topper = students[0]
lowest = students[0]

for student in students:
    if student["marks"] > topper["marks"]:
        topper = student

    if student["marks"] < lowest["marks"]:
        lowest = student

print("Topper:", topper["name"], "-", topper["marks"])
print("Lowest Scorer:", lowest["name"], "-", lowest["marks"])