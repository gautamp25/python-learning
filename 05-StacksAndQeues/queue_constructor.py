"""
    Queue:
        FIFO- First In First Out.
        enqueue - add
        dequeue - remove

        Removing an item from a Queue is O(1):

        List: In list removing & adding from the end of the list is O(1)
            and from other end adding & removing is O(n)

        Linked List- Removing from end is O(n) and adding back is O(1)
            and from other end adding & removing is O(1)

"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_queue = Queue(1)
my_queue.print_queue()