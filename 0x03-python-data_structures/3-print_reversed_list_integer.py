#!/usr/bin/python3
# reversed_list_printer.py

def print_reversed_list_integer(input_list=[]):
    """Prints all integers from a list in reverse order."""
    if isinstance(input_list, list):
        input_list.reverse()
        for i in input_list:
            print("{:d}".format(i))

