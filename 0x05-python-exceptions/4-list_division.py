#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            first = my_list_1[i]
            second = my_list_2[i]

            if not isinstance(first, int) or not isinstance(second, int):
                raise TypeError("wrong type")
            if second == 0:
                raise ZeroDivisionError("division by 0")

            div = first / second
            result.append(div)
        except IndexError as error:
            print(error)
            result.append(0)
        except TypeError as error:
            print(error)
            result.append(0)
        except ZeroDivisionError as error:
            print(error)
            result.append(0)
    return result
