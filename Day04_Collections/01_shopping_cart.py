"""
Problem Statement: Manage an online shopping cart using Python lists and list methods.

Problem Description:
A customer adds products to an online shopping cart.

Create a list containing:

["Laptop", "Mouse", "Keyboard", "Headphones"]

Perform the following:

Add "USB Cable" to the cart.
Remove "Keyboard".
Add "Monitor" at position 2.
Display the final cart.
Display the total number of products.

Concepts: list, append(), insert(), remove(), len()
"""

# Shopping Cart Application Using List

cart=[] # Create an empty cart initially

# ask user to enter product names to add in the cart
print("="*15,"Welcome to Shop with Joy","="*15)

N = int(input("No of Items You Purchased today: ").strip())

print("Enter Your Items Sequentially:")
for item in range(N):
    cart.append(input(f"Enter Item No. {item+1}").strip())

print(cart)

# add USB Cable to the list using append()

cart.append("USB Cable")

# removing Keyboard

cart.remove("Keyboard")

# Add Monitor at position 2
cart.insert(2,"Monitor")

#final Cart
print(cart)

print("No Of Products are ",len(cart))


print("="*30)