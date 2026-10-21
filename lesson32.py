
import json
import os

FILE_NAME = "students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read student data. Starting with an empty list.")
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = int(input("Enter marks (0-100): "))
    except ValueError:
        print("Please enter a whole number.")
        return

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    students.append({"name": name, "marks": marks})
    save_students(students)
    print("Student added and saved successfully!")


def view_students(students):
    if not students:
        print("No students available.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("----------------")


students = load_students()

while True:
    print("\n--- Student Management System ---")
    print("1. View Students")
    print("2. Add Student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
