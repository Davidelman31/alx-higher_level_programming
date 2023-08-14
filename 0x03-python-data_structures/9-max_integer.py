#!/usr/bin/python3
# 9-max_integer.py

def max_integer(input_list=[]):
    """Find the largest integer in a list."""
    if len(input_list) == 0:
        return None

    largest = input_list[0]
    for num in input_list:
        if num > largest:
            largest = num

    return largest

