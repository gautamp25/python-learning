class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp  = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        """
            PSEUDO CODE:
                method pop(self):
                IF length attribute is 0:
                        RETURN None
                SET temp to tail attribute
                IF length attribute is 1:
                    SET head to None
                    SET tail to None
                ELSE:
                    SET tail to prev attribute of tail
                    SET next attribute of tail to None
                    SET prev attribute of temp to None
                decrement length by 1
                RETURN temp
        """
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None 
        self.length -=1
        return temp.value
    
my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(4)

print(my_dll.pop_first())
print(my_dll.pop_first())
print(my_dll.pop_first())
print(my_dll.pop_first())
# my_dll.print_list()