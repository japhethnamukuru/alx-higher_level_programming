#!/usr/bin/python3
"""pythhon oop, working with classes"""


class Node():
    """A class that attempts to model a singly-linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_data = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("value must be a Node object")
        self.__next_node = value

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value


class SinglyLinkedList():
   """class that attempts to model a singly linked list"""
   
   def __init__(self):
       self.__head = None

   def sorted_insert(self, value):
       new_node = Node(value)
       if self.__head is None:
          new_node.next_node = None
          self.__head = new_node
       elif self.__head.data > value:
          new_node.next_node = self.__head
          self.__head = new_node
       else:
          tmp = self.__head
          while (tmp.next_node is not None and tmp.next_node.data < value):
            tmp = tmp.next_node
          new_node.next_node = tmp.next_node
          tmp.next_node = new_node

   def __str__(self):
       values = []
       tmp = self.__head
       while tmp is not None:
           values.append(str(tmp.data))
           tmp = tmp.next_node
       return ('\n'.join(values)) 
