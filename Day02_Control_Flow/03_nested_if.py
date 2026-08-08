"""
Question:
Write a Python program that checks whether a person is eligible
to drive.

If the person's age is 18 or above, ask whether they have a
valid driving license.

Age < 18       -> Not eligible
Age >= 18 + license -> Can drive
Age >= 18 + no license -> Need a license
"""

name = str(input("Enter Your Name").strip())
age = int(input("Enter Your age").strip())

print("="*15,"Driving Eligibility","="*15)

if age >= 18:
    hasLicense = True if input("Already have License(Yes/No): ").strip().lower() == "yes" else False
    # hasLicense = input("Already have License(Yes/No): ").strip().lower() == "yes" # this is also valid
    if hasLicense:
        print("Congrats! You can drive")
    else:
        print("Though You are 18 but still Need a license to drive.")
else:
    print("Sorry! You are not Eligible")


print("="*30)