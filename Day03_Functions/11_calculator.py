"""
Mini Project:
Refactor the Day 2 calculator using functions.

Requirements:
- Create an add() function.
- Create a subtract() function.
- Create a multiply() function.
- Create a divide() function.
- Create a modulus() function.
- Use match-case to select the operation.
- Handle division by zero.
- Return and display the result.

Goal:
Convert the previous procedural calculator into
a function-based calculator.
"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    if b!=0:
        return a/b
    else:
        return "Division by Zero"

def modulus(a,b):
    if b!=0:
        return a%b
    else:
        return "Division by Zero"

print("="*30)
print("Calculator Operation".center(15))
print("="*30)

print("1. Add Two Numbers")
print("2. Subtract Two Numbers")
print("3. Multiply Two Numbers")
print("4. Divide Two Numbers")
print("5. Modulus of Two Numbers")

choice = int(input("Enter Your Choice"))

match choice:
    case 1:print(add(5,6))
    case 2:print(sub(7,8))
    case 3:print(multiply(7,9))
    case 4:print(division(5,2))
    case 5:print(modulus(4,2))
    case _:print("Invalisd Choice")
