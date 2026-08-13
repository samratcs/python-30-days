"""
Question:
Create a function greet(name, message) where message
has a default value of "Welcome to Python".

Test the function with and without providing the message.

Example:
greet("Samrat")
greet("Samrat", "Good Morning")
"""

def greet(name,message="Welcome to Python"):
    print(f"Hello {name}, {message}")


name=input("Enter Your Name: ")
message=input("Want to give any Message? ")
if message:
    greet(name,message)
else:
    greet(name)