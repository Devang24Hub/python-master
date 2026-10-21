
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

n = int(input("Enter a positive number: "))

total =0

for i in range(1, n + 1):
    total=total+i
print("Total:", total)
