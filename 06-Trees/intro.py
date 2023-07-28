"""
    Tree having nodes called Left & Right.
    
    like treee = {
        "value":4,
        "left": None,
        "right": None
    }
    Parent and Child.
    Full tree: Every node either points to zero or two nodes.

    Binary Search Tree:
        In binary tree if number is greater than node then it's going to go on the
        right of that node and if it's less than it's going to go on the left
        ofthat node.

    IMP:
        - If you take any node in the binary search tree,all nodes below it
            to the right are going to be greater than that node.
        - and everything on the left is going to be less than that node. 

    BST BIG O:
    2^1-1 = 1
    2^2 - 1 = 3
    O(log n) because it is very efficient
    O(log n) is achieved by doing divide and conquer

    Lookup()
    Insert()
    Remove()

    Question- If retrieval speed is not very important bcoz we're not going to
    go retrieve things very often.but we could have burst data coming in and we
    want to make sure nothing gets dropped,so we want this to be able to
    be added as quickly as possible then what is choice between Linked list and
    Binary search tree?
    Ans- Linked list is better for this situation.
    There is no data structure that is the best answer in all situation.

                LinkedList                      BST
    1. Insert() O(n)                            
    2. Lookup() O(n)                            O(log n)
    3. Remove() O(n)                            O(log n)

    - Binary Search Trees always have a better Big O than Linked Lists: False
    - Binary Search Trees use divide and conquer.

    - Adding an item to a Binary Search Tree is always log n: False
    - Omega (best case) and Theta (average case) are both (log n). However, worst case is O(n) and Big O measures worst case. The typically treat Binary Search Trees as O(log n) but technically they are O(n). 


"""