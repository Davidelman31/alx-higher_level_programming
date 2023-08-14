#!/usr/bin/python3
# remove_c_characters.py

def no_c(input_string):
    """Remove all occurrences of characters 'c' and 'C' from a string."""
    filtered_characters = [char for char in input_string if char.lower() != 'c']
    return "".join(filtered_characters)
