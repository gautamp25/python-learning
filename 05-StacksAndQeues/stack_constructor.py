"""
    STACK: 
        LIFO-Last In First Out
        Stacks are commonly implemented with either Lists or Linked Lists.

        Pushing an item onto a Stack is O(1):
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_stack = Stack(4)

my_stack.print_stack()