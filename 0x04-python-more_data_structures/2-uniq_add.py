#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)  # set collection with no duplicates
    result = 0
    for i in unique:
        result += i
    return result
