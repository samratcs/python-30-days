
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
    price=float(input("Enter Product Price"))
    
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
    return

def mostCheapest():
    return

def getAllCategory():
    return





# ask user to enter product names to add in the cart
print("="*15,"Welcome to XYZKart","="*15)
print("1. Entry Product Details")
print("2. Most Expensive Product")
print("3. Most Cheapest Product")
print("4. All Product Categories")
print("5. Exit")

while True:
    choice = int(input("Enter Your Chices: ").strip())
    match choice:
        case 1:createEntry()
        case 2:mostExpensive()
        case 3:mostCheapest()
        case 4:getAllCategory()
        case 5:exit(0)
        case _:print("Invalid Option")


print("="*30)