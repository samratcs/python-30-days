"""
Question:
Create a function calculate_bill(price, quantity, discount).

Calculate:

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount

Return the final amount.

Example:
Price: 500
Quantity: 3
Discount: 10%

Output:
Final Amount: 1350
"""

def calculate_bill(price, quantity, discount):
    subtotal = price * quantity
    discount_amount = subtotal * discount / 100
    final_amount = subtotal - discount_amount

    print("Final Amount:",final_amount)

# Ask User For User Input
price=float(input("Enter Product Price: "))
quantity=int(input("Enter Product Quantity: "))
discount=float(input("Enter Discount Percentage: "))

# uses of both positional and keyword. 
calculate_bill(price,discount=discount,quantity=quantity)

