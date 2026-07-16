"""
Assignment 2: Student Marks Validator

Create a program that accepts student marks.

Requirements:
- Accept marks between 0 and 100.
- Handle non-numeric input.
- Reject negative marks.
- Reject marks greater than 100.
- Display the final marks if valid.
Expected output:
Enter marks: 105
Error: Marks must be between 0 and 100.
"""

print("="*30)
print("Exception Handling -- Student Marks Validator".center(10))
print("="*30)


try:
    marks=float(input("Enter Student Marks(between 0 and 100): "))
    if marks < 0:
        print("Negatrive Marks Cant be Accepted.")
    elif marks > 100:
        print("Marks Cant be greater than 100.")
    else:
        print(f"Marks Given is:{marks:.2f}")
except ValueError:
    print("Error! Non Numeric Input Cant Be accepted")


print("="*30)
print("THANK YOU".center(10))
print("="*30)