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

# Ask the user to enter sentence:

Sentence = input("Enter a Sentence").strip()
# Total Characters
Total_Characters = len(Sentence)
# Total Words
Total_Words = len(Sentence.split())
# First Character
First_Character = Sentence[0]
# Last Character
Last_Character = Sentence[-1]
# Reverse Sentence
Reverse_Sentence = Sentence[::-1]
# Uppercase
Sentence_in_Uppercase = Sentence.upper()
# Lowercase
Sentence_in_Lowercase = Sentence.lower()
# Replace every space with _
updated = Sentence.replace(" ","_")

# Display Details
print("Given Sentece            :", Sentence)
print("Total Characters         :", Total_Characters)
print("Total Words              :", Total_Words)
print("First Character          :", First_Character)
print("Last Character           :", Last_Character)
print("Uppercase Characters     :", Sentence_in_Uppercase)
print("Lowercase Characters     :", Sentence_in_Lowercase)
print("Reversed Sentence        :", Reverse_Sentence)


print("==================================================")

print()


# =====================================================
# Question 5
# Password Strength Analyzer
# =====================================================

print("="*15,"Password Strength Analyzer", "="*15)

print()

# Ask the user to enter a password.
password = input("Enter a Password").strip()

print("="*15,"Password Strength Analyzer", "="*15)

# Display:

# password length
Password_Length = len(password)

# first character
First_Character = password[0]

#second character
Last_Character = password[-1]

# # No of digits
Number_of_Digits = sum(1 if char.isdigit() else 0 for char in password)

# No of uppercase characters
Number_of_Uppercase_Letters = sum(1 if 65 <= ord(char) <=90 else 0 for char in password)

# No of lowercase characters
Number_of_Lowercase_Letters = sum(1 if 97 <= ord(char) <=122 else 0 for char in password)

# finding out the no of special characters  
# another approach is using isalnum()
Number_of_Special_Characters = sum(1 if (
        32 <= ord(char) <= 47 or
        58 <= ord(char) <= 64 or
        91 <= ord(char) <= 96 or
        123 <= ord(char) <= 126
) else 0 for char in password)

# Bonus Challenge

# Check whether the password satisfies:

At_least_8_characters = True if Total_Characters >= 8 else False
Contains_one_uppercase_letter = True if Number_of_Uppercase_Letters >= 1 else False
Contains_one_lowercase_letter = True if Number_of_Lowercase_Letters >= 1 else False
Contains_one_digit = True if Number_of_Special_Characters >= 1 else False



print("Password Length          :",Password_Length)
print("First Character          :",First_Character)
print("Last Character           :",Last_Character)
print("No Of Digits             :",Number_of_Digits)

print("==================================================")

print()
