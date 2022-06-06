#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list) - 1
    if my_list is None or len(my_list) is 0:
        return None
    else:
        while i > 1:
            j = 0
            while j < i:
                if my_list[j] > my_list[j + 1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
                j += 1
            i -= 1
        print(my_list[-1])
