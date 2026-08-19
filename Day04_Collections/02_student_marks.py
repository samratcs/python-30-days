"""
Problem Statement: Store and analyze student marks using a Python dictionary.
Problem Description:

A school wants to store a student's marks.

Create a dictionary:

{
    "name": "Rahul",
    "math": 85,
    "science": 78,
    "english": 92
}

Perform the following:

Display the student's name.
Calculate total marks.
Calculate average marks.
Add a new subject "computer": 95.
Display the subject with the highest marks.

Concepts: dictionaries, keys(), values(), items()

Practice problem:
Take the student's name and marks for 5 subjects as input and generate a result summary.

"""

# Create an Empty Dictionary 
record={}

record["name"]=input("Enter Student Name").strip()

# Ask user to enter marks for 5 subject with their subject name
for i in range(5):
    subject = input("Enter Subject Name: ")
    marks = int(input("Enter Marks Number: "))
    record[subject]=marks

# Display the student's name.
print("Student Name: ", record["name"])

# Calculate total marks.
total_marks = 0
for val in record.values():
    if val.isDigit():
        total_marks+=val
print("Total Marks: ",total_marks)

# Calculate average marks. 

avg_marks = total_marks / 5
print("Avg Marks",avg_marks)
# Add a new subject "computer": 95. 

record["computer"]=95

print(record)

# Display the subject with the highest marks.

