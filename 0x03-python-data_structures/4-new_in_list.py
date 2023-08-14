#!/usr/bin/python3
# modified_list_element_replacer.py

def new_in_list(original_list, index, new_element):
    """Replace an element in a copied list at a specific position."""
    if index < 0 or index > (len(original_list) - 1):
        return original_list

    copied_list = [x for x in original_list]
    copied_list[index] = new_element
    return copied_list

