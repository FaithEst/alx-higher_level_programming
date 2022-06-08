#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        avg = 0
        total = 0
        for item in my_list:
            avg += item[0] * item[1]
            total += item[1]
        return avg/total
    else:
        return 0
