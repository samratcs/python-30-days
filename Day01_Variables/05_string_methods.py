# =====================================================
# Question 1
# Personal Information Formatter
# =====================================================

print("="*15,"Personal Information Formatter", "="*15)

print()

# Take the following input from the user:

Full_Name = input("Enter Your Full Name")
City = input("Enter Your City Name")
Profession = input("Enter Your Profession")

# Display:

print("================ PERSONAL DETAILS ================")

print("Original Name    :",Full_Name)
print("Uppercase        :",Full_Name.upper())
print("Lowercase        :",Full_Name.lower())
print("Title Case       :",Full_Name.title())
print("Length           :",len(Full_Name))

print("==================================================")

print()

# =====================================================
# Question 2
# Email Validator
# =====================================================

print("="*15,"Email Validator", "="*15)

print()

 # Ask the user to enter an email address.

EmailID = input("Enter Your Email")

# Convert to lowercase
EmailId = EmailID.lower()

print(EmailID)
# Remove extra spaces using strip()
EmailID = EmailID.strip()
print(EmailID)
# Count the number of characters
l = len(EmailID)
print(f"length of {EmailID} is {l}")
# Check whether the email contains "@"
isValid = "@" in EmailID
print("@ in Email:",EmailID)

#Check whether it ends with .com
checkValidity = EmailID.endswith(".com")
print("'.com' in Email:",checkValidity)


print("==================================================")

print()

# =====================================================
# Question 3
# Company ID Generator
# =====================================================

print("="*15,"Company ID Generator", "="*15)

print()

# Ask the user to enter:

First_Name = input("Enter Employee First Name")
Last_Name = input("Enter Employee Last Name")
Employee_ID = input("Enter Employee ID")

# Generate an Employee Code using string methods.

Employee_Code = First_Name[0:4].upper() + Last_Name[0:4].lower() + Employee_ID

Official_Mail = First_Name.lower() + "."+ Last_Name.lower()+ "@tcs.com"


print("First Name           :",First_Name)
print("Last Name            :",Last_Name)
print("Employee ID          :",Employee_ID)

print("Employee Code                :",Employee_Code)
print("Employee Official Mail       :",Official_Mail)



print("==================================================")

print()

# =====================================================
# Question 4
# Sentence Analyzer
# =====================================================

print("="*15,"Sentence Analyzer", "="*15)

print()

# Ask the user to enter:

Sentence = input("Enter a Sentence")
Total_Characters 
Total_Words
First_Character
Last_Character
Reverse Sentence
Sentence in Uppercase
Sentence in Lowercase
Replace every space with

print("==================================================")

print()