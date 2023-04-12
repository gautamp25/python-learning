class Employee:
	def __init__(self,department,title,salary,emp_id):
		self.department = department
		self.title = title
		self.salary = salary
		self.emp_id = emp_id
		
	# n emp 20 obj
	# print emp_id asc salary high sal top
employee_list = []

emp_obj = Employee("HR","Manish",10000,1)
emp_obj1 = Employee("HR","Gautam",10000,2)
employee_list.append(emp_obj1)
employee_list.append(emp_obj)

# sort_by_sal = sorted(employee_list,key=lambda d:d['HR'])
print(employee_list.salary)
# obj_dict = { emp for emp in emp_obj.employee_list}
# sort_by_sal = sorted(obj_dict)

		