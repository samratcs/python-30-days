"""
Assignment 1: Safe Calculator

Create a calculator that accepts two numbers and an operator.

Requirements:
- Support addition, subtraction, multiplication and division.
- Handle invalid numeric input.
- Handle division by zero.
- Display meaningful error messages.

Expected output:
-----------------------
Enter first number: 20
Enter second number: 0
Enter operator: /

Error: Cannot divide by zero.

"""

print("="*30)
print("Exception Handling -- Safe Calculator".center(10))
print("="*30)


try:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    opr=input("Enter operator:(+ or - or * or /) ")

    match opr:
        case "+":
            print("The Addition is",num1+num2)
        case "-":
            print("The Subtraction is",num1-num2)
        case "*":
            print("The Multiplication is",num1*num2)
        case "/":
            print("The Divition is",num1/num2)
        case _:print("Invalid Choice)")
except ZeroDivisionError:
    print("Error! Divide By Zero.")
except ValueError:
    print("Error! Value Error")


print("="*30)
print("THANK YOU".center(10))
print("="*30)