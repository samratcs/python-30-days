"""
Question:
Demonstrate the difference between local and global variables.

Requirements:
- Create a global variable.
- Create a local variable inside a function.
- Print both variables.
- Demonstrate where each variable can be accessed.

Also experiment with the global keyword.
"""

x=10

def add(y):
    x=12
    z=y+x
    print(z)
    print(x)

def sub(y):
    global x
    z=y-x
    print(z)
    print(x)


add(5)
sub(6)
    