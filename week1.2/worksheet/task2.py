# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

numbers.sort()

print(f"Minimum = {min(numbers)}")
print(f"Maximum = {max(numbers)}")
print(f"Mean = {sum(numbers) / len(numbers)}")

middle = len(numbers) // 2
if len(numbers) % 2 == 1:
    median = numbers[middle]
else:
    median = (numbers[middle - 1] + numbers[middle]) / 2

print(f"Median = {median}")
    