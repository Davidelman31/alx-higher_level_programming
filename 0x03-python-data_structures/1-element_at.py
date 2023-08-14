#!/usr/bin/python3
def get_element_at_index(input_list, index):
    if index < 0:
        return None
    elif index >= len(input_list):
        return None
    return input_list[index]

