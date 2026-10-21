product =[
    {"Name":"Laptop","Price":"55000"},
     {"Name":"Mouse","Price":"800"},
      {"Name":"Keyboard","Price":"1500"},
    ]
print(product[0]["Name"])
total=0
for products in product:
    print(products["Name"],"-",products["Price"])
    total=total+ int(products["Price"])
print(total)




