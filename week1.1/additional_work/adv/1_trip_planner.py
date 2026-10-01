"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")

distance_miles_input = float(input("How many miles will you travel? "))
time_hours_input = float(input("How many hours will the journey take? "))

# TODO: convert distance_miles_input and time_hours_input to numbers

# TODO: calculate the average speed in miles per hour

average_speed = distance_miles_input / time_hours_input

# TODO: print a summary message using an f-string

if distance_miles_input <= 0 or time_hours_input <= 0:
    print("Warning: Distance and time must be positive values.")
else:
    print(f"Your trip to {destination} will take {time_hours_input:.2f} hours, covering a distance of {distance_miles_input:.2f} miles. Your average speed will be {average_speed:.2f} miles per hour.")

# Extension: add validation for zero or negative values
