# =====================================================
# Question 1
# Identify Python Data Types
# =====================================================

print("="*15,"DATA TYPES", "="*15)

print()

# Variable to store Integer Value
age = 24

# Variable to store Float Value
height = 6.2

# Variable to store String Value
name = "Samrat"

# Variable to store Boolean Value
isStudent = True

# Variable to store Complex Value
complex_num = 2+6j

print("Age                  :",age)
print("Data Type            :",type(age))
print()

print("Height               :",height)
print("Data Type            :",type(height))
print()

print("Name                 :",name)
print("Data Type            :",type(name))
print()

print("Student              :",isStudent)
print("Data Type            :",type(isStudent))
print()

print("Complex Number       :",complex_num)
print("Data Type            :",type(complex_num))
print()

print("-"*50)


# =====================================================
# Question 2
# Student Skills (Collection Data Types)
# =====================================================

print("="*15,"Student Skills (Collection Data Types)", "="*15)

print()

# Creating List Data Structure to store five programming languages
program_language = ["Python", "Java", "Dart", "C++", "C"]

# Creating Tuple Data Structure to store five database names
databases = ("MongoDB", "MySQL", "SQL Server", "IBM DB2", "Postress SQL")

# Creating Set Data Structure to store software development tools
software_tools = {"PyCharm", "IntelliJ Idea", "VS Code", "Postman", "WebStrom"}

# Creating Dictionary Data Structure to store student information.
student_info = {
    "name":"Samrat Sur",
    "Roll": "3434-61-0007",
    "age": 20,
    "course": "Computer Science",
    "city": "Howrah",
    "percentage": 65.50
}

print("Five Programming Languages:")
print(program_language)
print(type(program_language))
print()

print("Five Databases:")
print(databases)
print(type(databases))
print()

print("Five Software Tools:")
print(software_tools)
print(type(software_tools))
print()

print("Student Information:")
print(student_info)
print(type(student_info))
print()

print("-"*50)