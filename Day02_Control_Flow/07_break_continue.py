"""
Question:
Write a Python program that prints numbers from 1 to 100.

Requirements:
- Skip every number divisible by 5 using continue.
- Stop the loop when the number reaches 80 using break.


Expected sequence:
1 2 3 4 6 7 8 9 11 ...
"""

print("="*15,"Print 1 to 100 with condition","="*15)

for i in range(1,101):
    if i == 80:
        break
    if i % 5 == 0:
        continue

    print(i,end=", ")

print("="*30)