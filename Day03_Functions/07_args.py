"""
Question:
Create a function that accepts any number of numbers
using *args and returns their total sum.

Example:
calculate_sum(10, 20, 30, 40, 50)

Output:
150
"""

def calculate_sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(calculate_sum(10,20,30,40,50))
print(calculate_sum(1,3,5,7))
print(calculate_sum(2,4,6,8,10,12))