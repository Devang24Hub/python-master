
import json

students = [
    {"name": "Devang", "marks": 85},
    {"name": "Rahul", "marks": 78},
    {"name": "Priya", "marks": 92}
]

# Save student records to a JSON file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Student records saved successfully!")

# Load student records from the JSON file
with open("students.json", "r") as file:
    loaded_students = json.load(file)

print("\nLoaded Student Records:")

for student in loaded_students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("----------------")
