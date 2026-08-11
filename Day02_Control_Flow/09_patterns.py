"""
Question:
Write a Python program using nested loops to print
the following right-angled triangle:

*
**
***
****
*****
"""

print("="*15,"Star Pattern","="*15)

for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

print("="*30)