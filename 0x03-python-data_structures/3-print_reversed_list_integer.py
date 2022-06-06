#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1

    while i > 1:
        j = 0
        while j < i:
            if my_list[j] < my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            j += 1
        i -= 1
    for k in my_list:
        print(k)
