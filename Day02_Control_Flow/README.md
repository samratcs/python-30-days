# 🐍 Day 02 — Python Control Flow

This is **Day 2** of my **30 Days of Python** learning journey.

Today I am learning how to control the flow of a Python program using **conditional statements, loops, and loop-control statements**.

---

## 🎯 Learning Objectives

By the end of Day 2, I will understand:

* `if` statement
* `if-else`
* `if-elif-else`
* Nested `if`
* `match-case`
* `for` loop
* `while` loop
* `break`
* `continue`
* Nested loops
* Basic pattern printing
* Problem-solving using control flow

---

## 📂 Files

| File                   | Topic            | Question                                              |
| ---------------------- | ---------------- | ----------------------------------------------------- |
| `01_if_else.py`        | If-Else          | Check whether a number is positive, negative, or zero |
| `02_elif.py`           | If-Elif-Else     | Calculate grade based on marks                        |
| `03_nested_if.py`      | Nested If        | Check driving eligibility using age and license       |
| `04_match_case.py`     | Match-Case       | Build a simple calculator                             |
| `05_for_loop.py`       | For Loop         | Print multiplication table                            |
| `06_while_loop.py`     | While Loop       | Reverse a number                                      |
| `07_break_continue.py` | Break & Continue | Skip multiples of 5 and stop at 80                    |
| `08_nested_loop.py`    | Nested Loop      | Print a 5 × 5 number grid                             |
| `09_patterns.py`       | Pattern Printing | Print a right-angled star triangle                    |
| `exercises.py`         | Problem Solving  | Build a number guessing game                          |
| `atm_simulator.py`     | Mini Project     | Build a command-line ATM simulator                    |

---

# 1️⃣ If-Else

### File

```text
01_if_else.py
```

### Question

Write a Python program that accepts a number from the user and checks whether the number is positive, negative, or zero.

### Example

```text
Enter a Number: 10
Number is Positive
```

```text
Enter a Number: -5
Number is Negative
```

```text
Enter a Number: 0
Number is Zero
```

### Concept

```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

---

# 2️⃣ If-Elif-Else

### File

```text
02_elif.py
```

### Question

Accept marks from the user and determine the student's grade.

|    Marks | Grade |
| -------: | :---- |
|   90–100 | A+    |
|    80–89 | A     |
|    70–79 | B     |
|    60–69 | C     |
|    50–59 | D     |
| Below 50 | F     |

### Example

```text
Enter marks: 85
Grade: A
```

### Concept

```python
if condition:
    ...
elif condition:
    ...
else:
    ...
```

---

# 3️⃣ Nested If

### File

```text
03_nested_if.py
```

### Question

Create a program that checks whether a person is eligible to drive.

Rules:

* If age is below 18 → Not eligible
* If age is 18 or above → Check for driving license
* If the person has a license → Can drive
* Otherwise → Need a driving license

### Example

```text
Enter age: 22
Do you have a driving license? yes

You can drive.
```

### Concept

An `if` statement inside another `if` statement is called a **nested if**.

---

# 4️⃣ Match-Case

### File

```text
04_match_case.py
```

### Question

Create a simple calculator using `match-case`.

The program should accept:

1. First number
2. Operator
3. Second number

Supported operators:

```text
+
-
*
/
%
```

### Example

```text
Enter first number: 20
Enter operator: *
Enter second number: 5

Result: 100
```

The program should also handle division by zero.

### Concept

```python
match operator:
    case "+":
        ...
    case "-":
        ...
    case "*":
        ...
    case "/":
        ...
    case _:
        ...
```

---

# 5️⃣ For Loop

### File

```text
05_for_loop.py
```

### Question

Accept a number from the user and print its multiplication table from 1 to 10.

### Example

```text
Enter a number: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

### Concept

```python
for i in range(1, 11):
    ...
```

---

# 6️⃣ While Loop

### File

```text
06_while_loop.py
```

### Question

Accept an integer from the user and reverse the number using a `while` loop.

### Example

```text
Input: 12345
Output: 54321
```

### Concept

A `while` loop continues executing as long as its condition is `True`.

```python
while condition:
    # code
```

---

# 7️⃣ Break and Continue

### File

```text
07_break_continue.py
```

### Question

Write a program that prints numbers from 1 to 100.

Requirements:

* Skip numbers divisible by 5 using `continue`.
* Stop the loop when the number reaches 80 using `break`.

### Concept

#### `continue`

Skips the current iteration.

```python
if condition:
    continue
```

#### `break`

Terminates the loop.

```python
if condition:
    break
```

---

# 8️⃣ Nested Loop

### File

```text
08_nested_loop.py
```

### Question

Use nested loops to print the following 5 × 5 number grid:

```text
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

### Concept

A loop inside another loop is called a **nested loop**.

```python
for i in range(...):
    for j in range(...):
        ...
```

---

# 9️⃣ Pattern Printing

### File

```text
09_patterns.py
```

### Question

Use nested loops to print the following pattern:

```text
*
**
***
****
*****
```

### Concept

Pattern problems help understand:

* Nested loops
* `range()`
* Iteration
* Number of rows
* Number of columns

---

# 🔟 Problem Solving

### File

```text
exercises.py
```

### Question

Create a **Number Guessing Game**.

Requirements:

1. Store a secret number in the program.
2. Ask the user to guess the number.
3. If the guess is too high, display `Too high`.
4. If the guess is too low, display `Too low`.
5. Continue until the correct number is guessed.
6. Display the number of attempts.

### Example

```text
Guess the number: 30
Too low

Guess the number: 50
Too high

Guess the number: 42
Correct!

You took 3 attempts.
```

---

# 🚀 Mini Project — ATM Simulator

### File

```text
atm_simulator.py
```

### Question

Build a command-line ATM simulator.

Start with:

```python
balance = 10000
```

Display:

```text
===== ATM MENU =====

1. Check Balance
2. Deposit
3. Withdraw
4. Exit
```

### Requirements

#### 1. Check Balance

Display the current account balance.

#### 2. Deposit

Ask the user for an amount and add it to the balance.

#### 3. Withdraw

Ask the user for an amount.

If sufficient balance exists:

```text
Withdrawal successful.
```

Otherwise:

```text
Insufficient balance.
```

#### 4. Exit

Terminate the program.

#### 5. Invalid Choice

Display:

```text
Invalid choice. Please try again.
```

---

## 🔥 ATM Challenge

After completing the basic version, improve the project by adding:

* PIN authentication
* Maximum 3 PIN attempts
* Transaction history
* Deposit counter
* Withdrawal counter
* Minimum withdrawal amount
* Maximum withdrawal limit

---

# 🧠 Key Concepts Learned

```text
Conditional Statements
        ↓
    if / elif / else
        ↓
     Nested if
        ↓
    match-case
        ↓
       Loops
        ↓
   for / while
        ↓
 Loop Control Statements
        ↓
 break / continue
        ↓
    Nested Loops
        ↓
 Pattern Problems
        ↓
 Problem Solving
        ↓
    Mini Project
```

---

# 📝 Day 2 Practice Checklist

* [ ] Understand `if`
* [ ] Understand `if-else`
* [ ] Understand `elif`
* [ ] Understand nested `if`
* [ ] Understand `match-case`
* [ ] Understand `for` loop
* [ ] Understand `while` loop
* [ ] Understand `break`
* [ ] Understand `continue`
* [ ] Understand nested loops
* [ ] Complete pattern problem
* [ ] Complete number guessing game
* [ ] Complete ATM simulator
* [ ] Test programs with different inputs
* [ ] Commit all files to GitHub

---

# 📌 Git Commit

Suggested Day 2 commits:

```bash
git add README.md
git commit -m "Day 2: Add Python control flow notes"

git add 01_if_else.py
git commit -m "Day 2: Add if-else number classification"

git add 02_elif.py
git commit -m "Day 2: Add grade classification using elif"

git add 03_nested_if.py
git commit -m "Day 2: Add nested if driving eligibility"

git add 04_match_case.py
git commit -m "Day 2: Add match-case calculator"

git add 05_for_loop.py
git commit -m "Day 2: Add multiplication table using for loop"

git add 06_while_loop.py
git commit -m "Day 2: Add number reversal using while loop"

git add 07_break_continue.py
git commit -m "Day 2: Add break and continue practice"

git add 08_nested_loop.py
git commit -m "Day 2: Add nested loop number grid"

git add 09_patterns.py
git commit -m "Day 2: Add star pattern using nested loops"

git add exercises.py
git commit -m "Day 2: Add number guessing game"

git add atm_simulator.py
git commit -m "Day 2: Add ATM simulator mini project"
```

---

## ✅ Day 2 Completion

**Day 2 = Control Flow**

You should finish the day being able to take a problem and decide:

```text
Is there a decision?
      ↓
    if/elif/else

Do I need repetition?
      ↓
    for / while

Should I stop the loop?
      ↓
      break

Should I skip an iteration?
      ↓
    continue

Do I need a loop inside a loop?
      ↓
    nested loop
```

**Next → Day 3: Python Functions** 🐍
