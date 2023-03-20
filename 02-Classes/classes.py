class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    
obj1 = Cookie("Brown")
obj2 = Cookie("Green")
print(obj1.get_color(),obj2.get_color())

obj1.set_color("Yellow")
print("Obj1 cookie color is now", obj1.get_color())
print("Obj2 cookie color is still", obj2.get_color())