# Week 4, Session 2: Task 2

# Given an incomplete function odd_even and a docstring.
# Your task is to complete the function based on the details
# in the docstring.


def odd_even(lstIntegers):
    """
    This function takes a list of integers and returns the number of
    odd numbers and the number of even numbers in a list.

    Args:
        lstIntegers (list): A list of integers.

    Returns:
        list: A list containing [odd_count, even_count].
    """

    # Complete your code here
    odd_nums = list()
    even_nums = list()
    for i in lstIntegers:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    
    return [len(odd_nums), len(even_nums)]
# Check if correct output is produced
print(odd_even([0, 1, 2, 3, 4, 5, 6]))  # Output: [3, 2]
