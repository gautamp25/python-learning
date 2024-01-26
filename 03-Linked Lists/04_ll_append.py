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
        """
            Pseudo Code:
                METHOD print_list():
                # Set a temporary pointer to the head of the list

                set temp to head of the list

                #  Iterate through the list
                while temp is not None:
                    #  Print the value of the current node
                    print temp.value
                    #  Move the temporary pointer to the next node
                    set temp to temp.next
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    
    def append(self,value):
        """
        REMEMBER-Last and tail points to new node..
            Pseudo Code:
                METHOD append (value):
                    CREATE new_node with Node class and value

                    IF head attribute is None or length is 0:
                        SET head attribute to new_node
                        #SET tail attribute to new_node
                    ELSE:
                        SET next attribute of tail to new_node
                        #SET tail attribute to new_node
                    SET tail attribute to new_node (This shifted to outside coz it is common)
                    INCREMENT length attribute by 1
        """
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
    
my_linked_list = LinkedList(1)

my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.append(6)

my_linked_list.print_list()