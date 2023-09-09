#!/usr/bin/python3
def new_in_list(my_list, idx, element): 
    list_cpy = list(my_list)
    if idx < 0 or idx not in range(len(my_list)):
            return my_list
    list_cpy[idx] = element
    return list_cpy
