#!/usr/bin/python3
def uniq_add(my_list=[]):
    check = set()
    new_list = []
    result = 0

    for i in my_list:
        if i not in check:
            new_list.append(i)
            check.add(i)

    for add in range(len(new_list)):
        result += new_list[add]
    return result
