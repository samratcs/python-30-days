"""
Question:
Create a number guessing game.

Requirements:
1. Store a secret number in the program.
2. Ask the user to guess the number.
3. If the guess is too high, print "Too high".
4. If the guess is too low, print "Too low".
5. Continue until the user guesses correctly.
6. Display the number of attempts taken.

Example:

Secret number: 42
Guess: 30
Output: Too low

Guess: 50
Output: Too high

Guess: 42
Output: Correct! You took 3 attempts.
"""
import random
# Create a Number Guessing Game.

# Store a secret number in the program.
secret = random.randint(1,100)

# Ask the user to guess the number.
number = int(input("Enter Your Guessing Number(1-100)"))
count = 0
status = False
while status!=True:
    count += 1
    if number > secret:
        print("Guess Too High")
    if number < secret:
        print("Guess Too Low")
    if number == secret:
        print("Your Guess is Correct")
        print("No of Attempt: - ",count)
        status = True
    # ask again from user
    number = int("Enter Your Guessing Number(1-100) again")

    
