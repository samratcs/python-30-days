"""
Question:
Write a Python program that accepts marks from 0 to 100
and prints the student's grade.

90-100 -> A+
80-89  -> A
70-79  -> B
60-69  -> C
50-59  -> D
Below 50 -> F
"""

number = int(input("Enter Student Marks from 0 to 100"))

print("="*15,"Student Grade","="*15)

if 0 <= number <=100:
    if 90 <= number <= 100:
        print("A+")
    elif 80 <= number <= 89:
        print("A")
    elif 70 <= number <= 79:
        print("B")
    elif 60 <= number <= 69:
        print("C")
    elif 50 <= number <= 59:
        print("D")
    else:
        print("F")
else:
    print("Invalid Input")


print("="*30)

