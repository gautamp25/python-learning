class A:
    def method(self):
        print("A.method() called")

class B(A):
    def method(self):
        print("B.method() called")

# class C(A, B):
#     def __init__(self) -> None:
#         super().__init__(A)
#         super().__init__(B)
#         pass

# class D(C,B):
#     pass

# d=D()
# d.metho()