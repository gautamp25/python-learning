"""
    Over-riding built-in functions-
        Whenever we call print method then by default built-in __str__ method call internally.

"""

class Cart:
    # pass
    def __str__(self) -> str:
        return "This is cart object str method"


c_obj = Cart()
# with no method inside class
# print(c_obj) # <__main__.Cart object at 0x00000110D17D4C40>
print(c_obj) # This is cart object str method

class MyCart:
    def __init__(self,basket1, basket2,basket3):
        self.clothes = basket1
        self.electronics = basket2
        self.other = basket3

    def __len__(self):
        print("Total no.of item in cart:")
        return len(self.clothes)+len(self.electronics)+len(self.other)


my_cart_obj = MyCart(['pant','t-shirt','shirt'],['earphone','mobile'],['chair'])

print(len(my_cart_obj))