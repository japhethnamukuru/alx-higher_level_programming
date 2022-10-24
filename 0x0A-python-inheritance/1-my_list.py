#!/usr/bin/python3

"""python OOP, class that inherits from list"""


class MyList(list):
    """custom class that inheits from pythons list class"""

    def print_sorted(self):
        """sort the list in ascending order"""

        print(sorted(self))
