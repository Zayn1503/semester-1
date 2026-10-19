# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())

# Why does this work?
# As while fruit just checks if the list is not empty, and pop() removes the last item from the list until it is empty.

# What features of Python does it rely on?
# While loops, lists, and the pop method
