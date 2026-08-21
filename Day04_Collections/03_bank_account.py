"""
Problem Statement : Implement basic bank account operations using a Python dictionary.

Problem Description :

A bank stores account information using a dictionary.

account = {
    "name": "Sam",
    "account_number": "12345",
    "balance": 25000
}

Implement:

Deposit money.
Withdraw money.
Display balance.
Prevent withdrawal if the amount is greater than the balance.

Concepts: dictionary, conditional statements, updating values.

Practice problem:
Create a simple menu-driven banking system:
1. Deposit
2. Withdraw
3. Check Balance
4. Exit

"""
# initialize dictionary
data={}
# functions as follows



# ask user to enter product names to add in the cart
print("="*15,"Welcome to XYZ Bank","="*15)
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")

while True:
    choice = int(input("Enter Your Chices: ").strip())
    match choice:
        case 1:deposit()
        case 2:withdraw()
        case 3:getBalance()
        case 4:exit(0)
        case _:print("Invalid Option")


print("="*30)