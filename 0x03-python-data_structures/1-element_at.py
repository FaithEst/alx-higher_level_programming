#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_List) - 1:
        return None
    else:
        return my_list[idx]
