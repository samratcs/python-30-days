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

import random
import datetime

# initialize dictionary
accounts=[]

# functions as follows

def createAccount():
    name=input("Enter Account Holder name: ")
    mobile=input("Enter Your Mobile: ")
    account_number="XYZ_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    data={}
    data["name"]=name
    data["account_number"]=account_number
    data["mobile"]=mobile
    data["balance"]=0.0
    print("Your account opened successfully")
    print("-"*30)
    print("Account Holder:",data["name"])
    print("Account Number:",data["account_number"])
    print("Your Current Balance is:",data["balance"])
    accounts.append(data)
    return

def deposit():
    account_number = input("Enter Account Number: ")

    for account in accounts:
        if account["account_number"] == account_number:
            amount = float(input("Enter Deposit Amount: "))

            if amount > 0:
                account["balance"] += amount
                print("Amount deposited successfully!")
                print("Current Balance:", account["balance"])
            else:
                print("Deposit amount must be greater than 0.")
            return
    else:
        print("Account not found.")

def withdraw():
    account_number = input("Enter Account Number: ")
    
    for account in accounts:
        if account["account_number"] == account_number:
            amount = float(input("Enter Withdraw Amount: "))
    
            if account["balance"]-amount > 0:
                account["balance"] -= amount
                print("Amount deposited successfully!")
                print("Current Balance:", account["balance"])
            else:
                print("You dont Have sufficient amount of money in your account.")
            return
    else:
        print("Account not found.")

def getBalance():
    account_number = input("Enter Account Number: ")
        
    for account in accounts:
        if account["account_number"] == account_number:
            print("\n")
            print("Your Account Information".center(30))
            print("Account Holder:",account["name"])
            print("Account Number:",account["account_number"])
            print("Your Current Balance is:",account["balance"])
            print("\n")
            print("="*50)
            return
    else:
        print("Account Not Found")



# ask user to enter product names to add in the cart
print("="*15,"Welcome to XYZ Bank","="*15)
print("1. Account Opening")
print("2. Deposit")
print("3. Withdraw")
print("4. Check Balance")
print("5. Exit")

while True:
    choice = int(input("Enter Your Chices: ").strip())
    match choice:
        case 1:createAccount()
        case 2:deposit()
        case 3:withdraw()
        case 4:getBalance()
        case 5:exit(0)
        case _:print("Invalid Option")

