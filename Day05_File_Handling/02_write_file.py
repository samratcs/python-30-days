"""
Take the user's:
    Name
    Age
    City

and save them into a text file using with open().

"""

print("="*30)
print("File Handling -- Write File".center(10))
print("="*30)

Name = input("Enter Your Name: ")
Age = int(input("Enter Age: "))
City = input("Enter Your City: ")

with open("data.txt", "w") as file:
    lines = [Name, str(Age), City]
    file.writelines(lines)
    file.close()
    print("Data is written in the file.")

