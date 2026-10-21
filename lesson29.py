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


def search_student():
    name = input("Enter name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def class_average():
    if len(students) == 0:
        print("No students available.")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)
    print("Class Average:", round(average, 2))


while True:
    print("\n--- Student Management System ---")
    print("1. View Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Calculate Class Average")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        class_average()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")