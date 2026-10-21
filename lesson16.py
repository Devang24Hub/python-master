
def calculate_total(products):
    total = 0

    for product in products:
        total = total + product["Price"]

    return total


products = [
    {"Name": "Phone", "Price": 20000},
    {"Name": "Headphones", "Price": 2000},
    {"Name": "Charger", "Price": 1000}
]

result = calculate_total(products)
print("Total price:", result)
