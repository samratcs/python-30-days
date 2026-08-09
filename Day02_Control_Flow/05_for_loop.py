"""
Question:
Write a Python program that accepts a number from the user
and prints its multiplication table from 1 to 10.

Example:
Input: 5

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""

# ask user for the input for printing multiplication table 
number = int(input("Enter a Number").strip())


print("="*15,"01 - Multiplication Table","="*15)

for i in range(1,11):
    print(f"{number} x {i} = {number*i}")

print("="*30)


# Print numbers from 1 to 100.

print("="*15,"02 - Print 1 to 100","="*15)

for i in range(1,101):
    print(i,end=" ")

print("="*30)

# Print all even numbers from 1 to 100.

print("="*15,"03 - Print all even numbers from 1 to 100","="*15)

for i in range(1,101):
    if i % 2 == 0:
        print(i,end=" ")

print("="*30)

# Print all odd numbers from 1 to 100.

print("="*15,"04 - Print all odd numbers from 1 to 100","="*15)

for i in range(1,101):
    if i % 2 != 0:
        print(i,end=" ")

print("="*30)


# Calculate the sum of numbers from 1 to n.

print("="*15,"05 - Calculate the sum of numbers from 1 to n","="*15)

n = int(input("Enter the value of n").strip())
sum = 0
for i in range(1,n+1):
    sum+=i

print("Sum = ",sum)

print("="*30)


# Calculate the factorial of a number.

print("="*15,"06 - Calculate the factorial of a number","="*15)

n = int(input("Enter the value of n to find Factorial").strip())
fact = 1
for i in range(1,n+1):
    fact*=i

print("Facorial is",fact)

print("="*30)


# Print all even numbers from 1 to 100.

print("="*15,"07 - Count how many numbers between 1 and 100 are divisible by 7","="*15)

count = 0
for i in range(1,101):
    if i % 7 == 0:
        count +=1
        print(i,end=" ")

print("Count = "+count)

print("="*30)