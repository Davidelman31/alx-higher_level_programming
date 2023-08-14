#!/usr/bin/python3

def check_divisible__by_2(input_list=[]):
    result_list = []
    for num in input_list:
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list

