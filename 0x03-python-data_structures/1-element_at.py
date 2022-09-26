#!/usr/bin/python3
def element_at(my_list, idx):
    """
    function that retrieves an element from a given index of
    a list like in C.
    """
    if my_list:
        if idx <= 0:
            return None
        elif idx > len(my_list):
            return None
        else:
            retrieved_element = my_list[idx]

        return retrieved_element

