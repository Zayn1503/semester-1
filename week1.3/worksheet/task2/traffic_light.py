"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""
import sys

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
pairs = list(states.items())

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

while True:
    for i in pairs:
        state = i[0]
        time = i[1]
    
        while time > 0:
            print(f"Time {systime:03} State {state}")

            if systime >= maxtime:
                sys.exit()

            time -= 1
            systime += 1
        

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14