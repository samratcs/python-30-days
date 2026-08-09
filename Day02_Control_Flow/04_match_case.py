"""
Question:
Create a simple calculator using match-case.

The program should accept:
1. First number
2. Operator (+, -, *, /, %)
3. Second number

Perform the selected operation and display the result.

Also handle division by zero.
"""

# ask user for the input 
first_number = int(input("Enter First Number").strip())
operator = input("Enter Operator from allowed list(+, -, *, /, %)").strip()
second_number = int(input("Enter Second Number").strip())

print("="*15,"Simple Calculator using Match-Case","="*15)

# logic for match case
match operator:
    case '+':
        result = first_number + second_number
    case '-':
        result = first_number - second_number
    case '*':
        result = first_number * second_number
    case '/':
        if second_number != 0:     
            result = first_number / second_number
        else:
            result = "Trying Division by zero. Error!!"
    case '%':
            if second_number != 0:     
                result = first_number % second_number
            else:
                result = "Trying Division by zero. Error!!"
    case '_':
        result="Invalid Operator Provided."

# print the result

print("Result is ", result)


print("="*15,"Driving Eligibility","="*15)