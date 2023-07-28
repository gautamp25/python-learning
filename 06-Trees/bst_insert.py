"""
create new node
if root == None then root = new_node
temp = self.root
while loop
    IF new_node == temp return False
    IF < left ELSE > right
    IF None insert new_node else move to next

"""


class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # create a new node with the given value
        new_node = Node(value) 
        # if the tree is empty, set the new node as the root   
        if self.root is None:    
            self.root = new_node
            return True
        # set a temporary node to the root of the tree
        temp = self.root          
        while (True):
            # if the value already exists in the tree, return False
            if new_node.value == temp.value:  
                return False
            # if the value is less than the temporary node's value, go left
            if new_node.value < temp.value:
                # if there's no left child, insert the new node as the left child   
                if temp.left is None:         
                    temp.left = new_node
                    return True
                # otherwise, continue iterating through the left subtree
                temp = temp.left 
            # if the value is greater than the temporary node's value, go right             
            else: 
                # if there's no right child, insert the new node as the right child                           
                if temp.right is None:        
                    temp.right = new_node
                    return True
                # otherwise, continue iterating through the right subtree
                temp = temp.right             

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)