
"""
Real-World Practice Problem:
Create a program to analyze products in an online store.

Requirements:
- Store product names and prices.
- Find the most expensive product.
- Find the cheapest product.
- Display all unique product categories.
"""
# create a list of products 
products = []

def createEntry():
    product_name=input("Enter Product Name: ")
    category=input("Enter Product Category: ")
    price=float(input("Enter Product Price: "))
    
    data={}
    data["product_name"]=product_name
    data["category"]=category
    data["price"]=price
    
    print("Product created successfully")
    print("-"*30)
    print("Product Name:",data["product_name"])
    print("Product Price:",data["price"])
    print("Product Category is:",data["category"])
    products.append(data)
    return

def mostExpensive():
    most_expensive_product = ""
    price = 0
    for item in products:
        if price < item["price"]:
            price = item["price"]
            most_expensive_product = item["product_name"]
            
    return most_expensive_product

def mostCheapest():
    most_cheapest_product = ""
    price = products[0]["price"]
    for item in products:
        if price > item["price"]:
            price = item["price"]
            most_cheapest_product = item["product_name"]
                
    return most_cheapest_product

def getAllCategory():
    categiories = []
    for item in products:
        categiories.append(item["category"])
    uniqueCategory = set(categiories)

    return uniqueCategory





# ask user to enter product names to add in the cart
print("="*15,"Welcome to XYZKart","="*15)
print("1. Entry Product Details")
print("2. Most Expensive Product")
print("3. Most Cheapest Product")
print("4. All Product Categories")
print("5. Exit")

while True:
    choice = int(input("Enter Your Choices: ").strip())
    match choice:
        case 1:createEntry()
        case 2:print(f"Most Expensive Product is {mostExpensive()}")
        case 3:print(f"Most Expensive Product is {mostCheapest()}")
        case 4:
            uniqueCategory = list(getAllCategory())
            print(uniqueCategory)
        case 5:exit(0)
        case _:print("Invalid Option")


    print("="*30)