"""
Question:
Write a Python program that accepts an integer and reverses
the number using a while loop.

Example:
Input: 12345
Output: 54321
"""
print("="*15,"Reverse using While Loop","="*15)

n = int(input("Enter the value of n to find Reverse").strip())
temp = n #store the valuer of n in temp
reverse = 0
while temp > 0:
    rem = temp % 10
    rev = rev*10 + rem

print("Reverse is",rev)

print("="*30)