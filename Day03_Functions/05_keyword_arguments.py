"""
Question:
Create a function that accepts name, age, and city.

Call the function using keyword arguments.

Example:
display_person(
    age=21,
    city="Kolkata",
    name="Samrat"
)

The order of the arguments should not matter.
"""

# Define User Function to Display User Information
def display_person(name,age,city):
    print(f"Hello {name}, Your age is {age} and you are from {city}")


# Ask User For User Input
name=input("Enter Your Name: ")
age=int(input("Enter Your Age: "))
city=input("Enter Your City: ")

# uses of Keyword areguments while calling the function
display_person(age=age,city=city,name=name)