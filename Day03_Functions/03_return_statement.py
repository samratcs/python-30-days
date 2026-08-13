"""
Question:
Create a function called add_numbers() that accepts
two numbers and returns their sum.

Example:
Input: 10, 20
Output: 30
"""

def add_num(num1, num2):
    return (num1+num2)

num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))

print(f"Result is {add_num(num1,num2)}")