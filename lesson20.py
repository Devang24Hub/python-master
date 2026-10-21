
'''try:
    no1 = int(input("Enter number 1: "))
    no2 = int(input("Enter number 2: "))

    ans = no1 / no2
    print("Your division result is:", ans)

except ValueError:
    print("Invalid input! Please enter numbers.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
.........

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program finished.")
    ....
'''

try:
    number = int(input("Enter your age: "))

except ValueError:
    print("Please enter a valid age.")

else:
    if number < 18:
        print("You are under 18.")
    else:
        print("You are 18 or older.")

finally:
    print("Age check completed.")
