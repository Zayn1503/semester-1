"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""
try:
    numerator_input = int(input("Enter the numerator: "))
    denominator_input = int(input("Enter the denominator: "))
    result = numerator_input / denominator_input
    print(f"The result is: {result}")
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.") 
