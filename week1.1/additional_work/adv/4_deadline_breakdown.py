"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""

minutes_remaining_input = int(input("Minutes remaining until the deadline: "))

days_remaining = minutes_remaining_input // (24 * 60)
hours_remaining = (minutes_remaining_input % (24 * 60)) // 60
minutes_remaining = minutes_remaining_input % 60

if minutes_remaining_input < 0:
    print("Warning: The deadline has already passed.")
else:
    print(f"{days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes remaining")

# TODO: convert the input to an integer
# TODO: calculate whole days, leftover hours, and remaining minutes
# TODO: print the breakdown using f-strings
# Extension: detect negative values and print a warning instead
