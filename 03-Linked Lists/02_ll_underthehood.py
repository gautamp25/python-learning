"""
1. Linked list does not have indexes.
2. List is contiguous place in memeory
Linked List and List
    1. Append- O(1)- O(1)
    2. Pop- O(n) - O(1)
    3. Prepend- O(1) - O(n)
    4. Pop First- O(1) - O(n)
    5. Insert- O(n) - O(n)
    6. Remove- O(n) - O(n)
    7. Look up by Index- O(n) - O(1)
    8. Look up by Value- O(n) - O(n)


Node: Value and Pointer both together make up node.It is essentially dictionary.
    {
        "value":4,
        "next":None
    }

    11 3 23 7 4
    head:{
        "value":11,
        "next":{
            "value":3,
            "next":{
                "value":23,
                "next":{
                    "value":7,
                    "next":{
                        "value":4,
    tail===========>    "next":None
                    }
                }
            }
        }
    }
    Nestead dictionaries
"""

head = {
        "value":11,
        "next":{
            "value":3,
            "next":{
                "value":23,
                "next":{
                    "value":7,
                    "next":{
                        "value":4,
                        "next":None
                    }
                }
            }
        }
    }
print(head["next"]["next"]["value"])
# This will Only run with a Linked List
# print(my_linked_list.head.next.next.value)