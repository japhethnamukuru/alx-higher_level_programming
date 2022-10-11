#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for item in my_list[:x]:
            print("{}".format(item), end='')
            i += 1
        print("\n")
    except TypeError:
        print("could not print items")
    else:
        return (i)
