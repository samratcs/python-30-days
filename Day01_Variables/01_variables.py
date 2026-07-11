# =====================================================
# Question 1
# Student Information
# =====================================================

# Student Information

# Variable stores student's name
student_name = "Samrat Sur"
# Variable stores student's age
age = 24
# Variable stores student's city
city = "Kolkata"
# Variable stores student's course
course = "Web Development"
# Variable stores student's percentage
percentage=80.0

print("="*16,"Student Details","="*16)

print("Student Name         : ",student_name)
print("Student Age          : ",age)
print("Student City         : ",city)
print("Student Course       : ",course)
print("Student Percentage   : ",percentage,"%")



print("-" * 50)


# =====================================================
# Question 2
# Rectangle Dimensions
# =====================================================

# Storing the length of rectangle
length=20
# storing the breadth of rectangle
breadth=15


print() 
#display Information
print("="*10,"Rectangle Dimensions","="*10)
print("Length       :",length)
print("Breadth      :",breadth)

#Calculate the area and perimeter of calculator
area=length*breadth
perimeter=2*(length+breadth)
print("Area is      :",area)
print("Perimeter is :",perimeter)


print("-" * 50)


# =====================================================
# Question 3
# Employee Information
# =====================================================

# Variable stores employee's name
employee_name = "Samrat Sur"
# Variable stores employee's id
employee_id = "E20345698"
# Variable stores employee's company
company_name = "Tata Consultancy Services"
# Variable stores employee's department
department = "BFSI IT"
# Variable stores employee's designation
designation = "Systems Engineer"
# Variable stores employee's work location
work_location = "TCS-Kolkata"
# Variable stores employee's years of experience
years_of_experience = 6
# Variable stores employee's monthly salary
monthly_salary = 25000
# Variable stores employee's email
email_id = "samratiafo@gmail.com"
# Variable stores employee's phone
phone_number = "9089789023"

# Calaculate the annual salary
annual_salary = monthly_salary * 12

# Calculate bonus 10% of annual Salary
bonus = annual_salary * 0.10

# Calculate total salary
total_salary = annual_salary + bonus

print("="*50)
print("\t\tEmployee Details\t\t")
print("="*50)

print()

print("Employee Name        :", employee_name)
print("Employee Id          :", employee_id)
print("Company Name         :", company_name)
print("Department           :", department)
print("Designation          :", designation)
print("Work Location        :", work_location)
print("Years of Experience  :", years_of_experience, "Years")
print("Email ID             :", email_id)
print("Phone Number         :", phone_number)

print("-" * 15, "Salary Details", "-" * 15)

print()
print(f"Monthly Salary       : ₹{monthly_salary}")
print(f"Annual Salary        : ₹{annual_salary}")
print(f"Bonus                : ₹{bonus:.2f}")
print(f"Total Salary         : ₹{total_salary:.2f}")

print("-" * 50)


# =====================================================
# Question 4
# Swap Two Variables
# =====================================================

# variables to store first number
value_1 = 3
# variables to store second number
value_2 = 5

# swap with using third variable using variable temp
print("="*10,"Swap Two Number Using Third Variable","="*10)
print()
print("Before Swapping")
print("Value 1  :", value_1)
print("Value 2  :", value_2)
temp = value_1
value_1 = value_2
value_2 = temp
print("After Swapping")
print("Value 1  :", value_1)
print("Value 2  :", value_2)

# swap with out using third variable
print("="*10,"Swap Two Number With out Using Third Variable","="*10)
print()
print("Before Swapping")
print("Value 1  :", value_1)
print("Value 2  :", value_2)
# logic for swapping
value_1 = value_1 + value_2
value_2 = value_1 - value_2
value_1 = value_1 - value_2
print("After Swapping")
print("Value 1  :", value_1)
print("Value 2  :", value_2)


print("-" * 50)


# =====================================================
# Question 5
# Mobile Phone Specifications
# =====================================================

# Write your solution here