#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for i in my_list:
        if idx not in range(my_list[i]):
            return None
        elif idx == my_list[i]:
            return my_list[i]
