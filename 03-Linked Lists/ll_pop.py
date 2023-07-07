"""
    take two variables temp & pre
    if temp.next is not None:
        temp = temp.next
        pre = temp
"""

class Node:
    """
        We have common create new Node in below class's every method so,
        we will create class instead for this.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        # create new Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self,value):
        # create new Node
        # add Node to end
        new_node = Node(value)
        # if self.head is None:
        if self.length == 0:
            self.head = new_node
            # self.tail = new_node
        else:
            self.tail.next = new_node
            # self.tail = new_node
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        """
        The pop method remove the last node (tail) from the linked list and return the removed node.
            1.If the list is empty, the method should return None. 
            2.After the last node is removed, the second-to-last node should become the new tail of the list.
            3.if the list becomes empty after the pop operation, both the head and tail attributes should be set to None.
            - Pseudo Code:
                METHOD pop:
                    IF length attribute is 0:
                        RETURN None

                    SET temp to head attribute
                    SET pre to head attribute

                    WHILE next attribute of temp is NOT None:
                        SET pre to temp
                        SET temp to next attribute of temp

                    SET tail attribute to pre
                    SET next attribute of tail to NULL
                    DECREMENT length attribute by 1

                    IF length attribute is 0:
                        SET head attribute to NULL
                        SET tail attribute to NULL

                    RETURN temp
        """
        # Pop return the last element from LL
        if self.length == 0:
            return None
        # Initially both pointing to head
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next 
        self.tail = pre 
        self.tail.next = None
        self.length -= 1
        # setting head & tail None
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

my_linked_list = LinkedList(1)

my_linked_list.append(2)

print(my_linked_list.pop()) # return Node 2

print(my_linked_list.pop()) # return Node 1

print(my_linked_list.pop()) # return None