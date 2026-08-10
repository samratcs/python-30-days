"""
Question:
Write a Python program using nested loops to print
a 5 x 5 grid of numbers.

Expected output:

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

print("="*15,"Print 5 x 5 Grid of Numbers","="*15)

for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

print("="*30)