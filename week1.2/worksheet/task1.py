# Worksheet 1.2: Task 1 Solution
import sys

error_message = "Error: Grade must be an integer between 0 and 100"
grade_input = input("Enter an integer grade between 0-100: ")

if not grade_input.isdecimal():
    sys.exit(error_message)

grade = int(grade_input)

if grade > 100:
    sys.exit(error_message)
elif grade < 40:
    print(f"{grade} is a Fail")
elif grade < 70:
    print(f"{grade} is a Pass")
else:
    print(f"{grade} is a Distinction")