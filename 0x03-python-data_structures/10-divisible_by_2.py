#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    multiple = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiple.append(True)
        else:
            multiple.append(False)

    return (multiple)
