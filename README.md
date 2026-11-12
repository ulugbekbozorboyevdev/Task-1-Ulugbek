# Password Strength Checker

A beginner-friendly Python program that evaluates password strength based on four security criteria.

## Overview

The Password Strength Checker analyzes a user-provided password and assigns a strength rating based on its characteristics.

The program checks whether the password meets four basic requirements and calculates a score out of 4.

## Features

- Checks whether the password contains at least 8 characters.
- Detects uppercase letters.
- Detects numeric digits.
- Checks for special characters.
- Calculates a password strength score.
- Classifies passwords as Weak, Medium, or Strong.

## Password Requirements

The program evaluates passwords using the following criteria:

| Requirement | Description | Points |
|---|---|---|
| Length | At least 8 characters | 1 |
| Uppercase | Contains an uppercase letter (A–Z) | 1 |
| Digit | Contains at least one number (0–9) | 1 |
| Special Character | Contains a symbol (e.g. @, #, !) | 1 |

## Strength Classification

The final score determines the password's strength:

| Score | Strength |
|---|---|
| 0–1 / 4 | Weak |
| 2–3 / 4 | Medium |
| 4 / 4 | Strong |

## Technologies Used

- **Python 3**
- Built-in Python functions and string methods, including `len()`, `any()`, `isupper()`, `isdigit()`, and `isalnum()`.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Clone this repository or download the project files.
3. Open a terminal in the project directory.
4. Run the Python file:

```bash
python main.py
```

5. Enter a password when prompted and view the result.

*Note: Replace `main.py` with your actual Python filename if it is different.*

## Project Purpose

This project was developed as part of my DecodeLabs internship tasks to practice Python fundamentals, conditional statements, Boolean logic, string manipulation, and built-in functions.

---

**Author:** Ulugbek Bozorboyev  
**Language:** Python
