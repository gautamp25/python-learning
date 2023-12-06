"""
    Polymorphism:
        - Polymorphism in python is an ability of python object to take many forms.
        - If a variable, method, object performs different behaviour
          according to situation is called Polymorphism.
        - example:  print(10+20) #30 addition
                    print("Hello"+"World") # HelloWorld  concatenation
"""

class Vehicle:
    def __init__(self,name,color,prize):
        self.name = name
        self.color = color
        self.prize = prize

    def get_details(self):
        print("Name is:", self.name)
        print("color is:", self.color)
        print("prize is:", self.prize)
    
    def max_speed(self):
        print(f"Max speed of {self.name} is 100")

    def gear(self):
        print("Total gear is 6")

class Car(Vehicle):
    def max_speed(self):
        print(f"Max speed of {self.name} is 140")

    def gear(self):
        print("Total gear is 5")
    
x = 3000000
print(f"{x:-}")
veh_obj = Vehicle("Truck","Red",3000000)
veh_obj.get_details()
veh_obj.max_speed()
print()
car_obj = Car("Altroz","Downtown Red",800000)
car_obj.get_details()
car_obj.max_speed()
car_obj.gear()