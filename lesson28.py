students = [
    {"name": "Devang", "marks": 85},
    {"name": "Rahul", "marks": 78},
    {"name": "Priya", "marks": 92}
]


def view_students():
    for student in students:
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("----------------")


def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    student = {"name": name, "marks": marks}
    students.append(student)

    print("Student added successfully!")


while True:
    print("\n--- Student Management System ---")
    print("1. View Students")
    print("2. Add Student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")