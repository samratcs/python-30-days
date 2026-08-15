"""
Lambda Function Practice — Day 3

Question 1: Square of a Number
--------------------------------
Create a lambda function that accepts a number
and returns its square.

Example:
Input: 5
Output: 25


Question 2: Find the Larger Number
-----------------------------------
Create a lambda function that accepts two numbers
and returns the larger number.

Example:
Input: 10, 25
Output: 25


Question 3: Check Even or Odd
------------------------------
Create a lambda function that accepts a number
and returns "Even" if the number is even,
otherwise returns "Odd".

Example:
Input: 7
Output: Odd


Question 4: Calculate Final Price
---------------------------------
Create a lambda function that accepts the product
price and discount percentage and returns the
final price after applying the discount.

Formula:
discount_amount = price * discount / 100
final_price = price - discount_amount

Example:
Price: 1000
Discount: 20%

Output:
800


Question 5: Sort Students by Marks
-----------------------------------
Given a list of students containing their names
and marks, use a lambda function with sorted()
to sort the students according to their marks
in ascending order.

Example:

students = [
    ("Samrat", 85),
    ("Rahul", 72),
    ("Priya", 95),
    ("Amit", 80),
    ("Sneha", 90)
]

Expected Output:

[
    ("Rahul", 72),
    ("Amit", 80),
    ("Samrat", 85),
    ("Sneha", 90),
    ("Priya", 95)
]


Bonus Challenge:
----------------
Modify the sorting logic to arrange the students
in descending order of their marks.

Expected Order:

Priya  - 95
Sneha  - 90
Samrat - 85
Amit   - 80
Rahul  - 72
"""



# Question 1: Square of a Number

square = lambda x:x**2
print(square(5))

# Question 2: Find the Larger Number

largest = lambda x,y: x if x>y else y
print(largest(5,7))

# Question 3: Check Even or Odd

isEvenOdd = lambda x: "Even" if x%2==0 else "Odd"
print(isEvenOdd(4))
print(isEvenOdd(5))

# Question 4: Calculate Final Price

final_amount = lambda price,discount: price-(price*(discount/100))
print(final_amount(1000,20))

# Question 5: Sort Students by Marks

students = [
    ("Samrat", 85),
    ("Rahul", 72),
    ("Priya", 95),
    ("Amit", 80),
    ("Sneha", 90)
]

result = sorted(students, key=lambda student: student[1])

print(result)

