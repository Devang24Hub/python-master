
print("===== SIMPLE CALCULATOR =====")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice.")
