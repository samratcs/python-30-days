"""
Create a text file containing several lines of text. Write a Python program to:

Open the file
Read the complete content
Display it
Count the number of lines
"""

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
    line_count = len(content.splitlines())
    print("No of Lines: ",line_count)
    word_count = len(content.split())
    print("No of Words:",word_count)
    char_count = len(content)
    print("No of Characters: ",char_count)
