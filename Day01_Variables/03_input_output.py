# =====================================================
# Question 1
# Student Registration Form
# =====================================================


Student_Name = input("Enter Student Name: ")
Age = int(input("Enter Student Age: "))
Gender = input("Enter Student Gender: ")
Email = input("Enter Student Email: ")
Phone_Number = int(input("Enter Student Phone No: "))
City = input("Enter Student City: ")
College_Name = input("Enter Student College Name: ")
Course = input("Enter Student Course: ")

print("="*15,"Student Registration Form", "="*15)

print()

print("Name                 :", Student_Name)
print("Age                  :", Age)
print("Gender               :", Gender)
print("Email                :", Email)
print("Phone Number         :", Phone_Number)
print("City                 :", City)
print("College Name         :", College_Name)
print("Course               :", Course)


print()

print("-"*50)

# =====================================================
# Question 2
# Employee Salary Calculator
# =====================================================

#Variables to Store employee Details
Employee_Name = input("Enter Employee Name: ")
Employee_ID = int(input("Enter Employee ID "))
Monthly_Salary = float(input("Enter Employee Monthly Salary: "))


# calculate bonus and total salary
Annual_Salary = Monthly_Salary * 12
Bonus = Annual_Salary * 0.10
Total_Salary = Annual_Salary + Bonus

print("="*15,"Employee Salary Calculator", "="*15)

print()

print(f"Annual Salary    :₹{Annual_Salary:,.2f}")
print(f"Bonus            :₹{Bonus:,.2f}")

print(f"Total Salary     :₹{Total_Salary:,.2f}")

print()

print("-"*50)

# =====================================================
# Question 3
# Online Shopping Bill
# =====================================================

Customer_Name = input("Enter Customer Name: ")
Product_Name = input("Enter Product Name: ")
Quantity = int(input("Enter Quantity "))
Price_per_Item = float(input("Enter Price Per Item: "))

# Calculate GST and Final Bill

Total_Price = Quantity * Price_per_Item
GST_Amt = Total_Price * 0.18
Final_Bill = Total_Price + GST_Amt

print("="*15,"Online Shopping Bill", "="*15)

print()

print("Customer Name                        :", Customer_Name)
print("Product Name                         :", Product_Name)

print(f"Quantity * Price Per Price           :{Quantity} * {Price_per_Item}")

print("-"*20, "Bill Information", "-"*20)
print(f"Total Price                          :₹{Total_Price:,.2f}")
print(f"GST                                  :₹{GST_Amt:,.2f}")

print(f"Final Bill                           :₹{Final_Bill:,.2f}")

print()

print("-"*50,end="\n\n")

# =====================================================
# Question 4
# Banking Application
# =====================================================

print("="*15,"Banking Application", "="*15)
Customer_Name = input("Enter Customer Name: ")
Account_Number = input("Enter Account Number: ")
Current_Balance = float(input("Enter Current Balance "))
Deposit_Amount = float(input("Enter Deposit Amount: "))
Withdraw_Amount = float(input("Enter Withdraw Amount: "))

# Calculation
print("-"*50)

print("="*15,"Account Information", "="*15)

print()

print("Customer Name                            :",Customer_Name)
print("Account Number                           :",Account_Number)
Current_Balance += Deposit_Amount
print(f"Balance after Deposit                   : {Current_Balance:,.2f}")
Current_Balance -= Withdraw_Amount
print(f"Final Balance after Withdrawal          : {Current_Balance:,.2f}")

print("-"*50)


# =====================================================
# Question 5
# Developer Portfolio Application
# =====================================================

print("="*15,"Developer Portfolio Builder", "="*15)

print()

# Personal Details 
Full_Name = input("Enter Full Name: ")
Email = input("Enter Email: ")
Phone_Number = input("Enter Your Phone Number: ") 
City = input("Enter Your City: ")

#Professional Details
Current_Company = input("Enter Your Current Company Name: ")
Designation = input("Enter Your Current Designation: ")
Years_of_Experience = int(input("Enter Your Total Years of Experience: "))
Expected_Salary = int(input("Enter Your Expected Salary: "))

# Technical Skills
skill_1 = input("Enter Your First Skill: ")
skill_2 = input("Enter Your Second Skill: ")
skill_3 = input("Enter Your Third Skill: ")

print("="*15,"Your Portfolio", "="*15)

print()

print("-"*10,"Basic Details","-"*10)
print("Name                     :",Full_Name)
print("Email                    :",Email)
print("Phone Number             :",Phone_Number)
print("City                     :",City)

print()

print("-"*10,"Professional Details","-"*10)

print("Current Company          :", Current_Company)
print("Designation              :", Designation)
print("Years of Experience      :", Years_of_Experience)
print("Expected Salary          :", Expected_Salary)

print("-"*10,"Skills","-"*10)

print("1.", skill_1)
print("2.", skill_2)
print("3.", skill_3)

print("-"*50)

