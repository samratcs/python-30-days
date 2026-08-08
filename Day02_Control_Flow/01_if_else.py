"""
Question:
Write a Python program that accepts an integer from the user
and checks whether the number is positive, negative, or zero.

Example:
Input: 10
Output: Positive number
"""
# ask user for a number
number = int(input("Enter a Number"))
# logic using if-else for number classification
if number > 0:
    print("Number is Positive")
else:
    print("Number is Negative or Zero")