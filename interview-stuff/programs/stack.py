
class Stack:
	
	def __init__(self):
		self.val_list = []
		self.min_val=0
		
	
	def push(self,item):
		if self.min_val>item:
			self.min_val=item
		self.val_list.append(item)
		
	def pop(self,item):
		self.val_list.pop(item)
		
	def get_minimum(self):
		return self.min_val

		
obj=Stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(0)
obj.pop(2)
# obj.push(-1)
# print(obj)
print(obj.get_minimum())
# print(a)

class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())   # output: 3
print(stack.peek())  # output: 2
print(stack.size())
