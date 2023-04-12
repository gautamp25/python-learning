# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 5
for i in range(n):
	for j in range(n-i+1):
		# for left spacing
		print(end=" ")

	for j in range(i+1):

		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	# for new line
	print()

n=5
for i in range(n):
	for j in range(i+1):
		print("*",end=" ")
	print("")

n=5	
k=n-1
for i in range(n):
	for j in range(n-1):
		print(" ", end =' ')
	# k+=1
	for j in range(i+1):
		print("*", end="")
	print()


rows = 5
k = 2 * rows - 2  # It is used for number of spaces  
for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 2   # decrement k value after each iteration  
    for j in range(0, i + 1):  
        print("* ", end="")  # printing star  
    print("") 

n=6
r=1
while r<=n:
	c=1
	while c<=n:
		if (c<=(n-r)):
			print(" ",end=' ')
		else:
			print("*",end=' ')
		c+=1
	r+=1
	print()
    


	
	
	
