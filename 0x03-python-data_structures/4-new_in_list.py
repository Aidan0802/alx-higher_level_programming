#!/usr/bin/python3
def new_in_list(my_list, idx, element): 
    list_cpy = my_list[:]
    if idx < 0 or idx not in range(len(my_list)):
            return my_list
    list_cpy[idx] = element
    return list_cpy



my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
