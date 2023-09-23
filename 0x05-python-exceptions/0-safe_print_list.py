#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if i > x:
                break
            print(i, end="")
            count += 1
    except e:
        print("Error: Element is not printable.")
    finally:
        print()
    return count
