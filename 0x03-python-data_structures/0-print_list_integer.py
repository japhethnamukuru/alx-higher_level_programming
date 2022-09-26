#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    function that prints all integers of a list.
    """
    if my_list:
        for num in my_list:
            print("{}".format(num))
