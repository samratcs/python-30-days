"""
Create a program that allows the user to enter student details and save them to a file.

Example:

Name: Rahul
Marks: 85

Name: Priya
Marks: 92

Then read the file and display all student records.
"""

print("="*30)
print("File Handling -- Student Records".center(10))
print("="*30)

students = []
N = int(input("Enter no of Students Data that you want to keep: ").strip())

for i in range(1,N+1):
    Name = input("Enter Student Name: ")
    Age = int(input("Enter Student Marks: "))
    students.append([Name, Age])

with open("students.txt", "w") as file:
    for student in students:
        file.write(f"Student Name: {student[0]}\n")
        file.write(f"Student Marks {student[1]}\n")
        file.write("\n\n")
    
    file.close()
    print("Data is written in the file.")

with open("students.txt", "r") as file:
    content = file.read()
    print(content)
    file.close()