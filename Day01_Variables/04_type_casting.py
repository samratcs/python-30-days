# =====================================================
# Question 1
# Student Age Converter
# =====================================================

print("="*15,"Student Age Converter", "="*15)

print()


# Takes the student's name. 
Full_Name = input("Enter Student Name: ")
# Takes the student's Age.
Age = input("Enter Age: ")


# Print the data type of the age before conversion.
print("Before Type Conversion Type of Student's Age is :",type(Age))
Designation = input("Enter Your Current Designation: ")

# Convert the age to an integer.
Age = int(Age)

# Print the data type after conversion.
print("After Type Conversion Type of Student's Age is :",type(Age))


Age = Age + 5

# Display the student's age after 5 years.
print("After % years Student's Age is :",Age)



print()

print("-"*50)

# =====================================================
# Question 2
# Product Price Calculator
# =====================================================

print("="*15,"Product Price Calculator", "="*15)

print()

Product_Name = input("Enter Student Name: ")
Product_Price = input("Enter Product Price: ")
Quantity = input("Enter Product Quantity: ")

# Convert to respective types
Product_Price = float(Product_Price)
Quantity = int(Quantity)

# Display all the information in a formatted report.
Total_Price = Product_Price * Quantity

# Calculate GST (18%) and Final Price.
Bonus = Total_Price * 0.18

Final_Price = Total_Price + Bonus

print()

print("-"*10,"Student Details","-"*10)
print("Total Price              :",Total_Price)
print("Bonus                    :",Bonus)
print("Final Price              :",Final_Price)

print()

print("-"*50)


