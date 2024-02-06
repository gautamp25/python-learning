        
"""
l1= [1,2]
t1= (1,2,3,4)
d1 = {'a':1,'b':3}
for i in t1:
    print(i)
    
__getattr__
__getattribute__

class Test:
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print()
        
    

obj = Test("Gautam")
print(obj)
        
        
from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return "Hello World"
    
if __name__=='__main__':   
    app.run("127.0.0.1", '5000')
    

def my_decor(fun):
    def test():
        fun()
        print("Test funcion")
    return test
    

def show():
    pass


my_str = "Gautam Patil"
# output={g: 1, a:3 }

def test(my_str):
    my_dict = {}
    for char in my_str:
        if char in my_dict:
            my_dict[char]+=1
        else:
            my_dict[char]=1
    print(my_dict)
    
test(my_str)

# useState()
# useEffect()
# useRef()
# useContext()
# useMemo()

select max(salary) from employee
where salary<(select max(salary) from employee)
"""

