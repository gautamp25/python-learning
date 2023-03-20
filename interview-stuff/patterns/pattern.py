# * * *
# * *
# *
# Approach
""" Observe the given pattern
1. Number of rows = Has 3 rows. have print pattern for N rows
2. Number of Cols = The no.of cols in any row is equal to (N-row+1). 1st row has col (3-1+1).
2nd row has col (3-2+1)and so on..
3. What to print = all entries in any row are "*" """
# n=int(input())
n=3
row = 1 

while row <= n:
    col = 1
    while col<=(n-row+1):
        print("*",end=" ")
        col+=1
    row+=1
    print()




"""
    *
  * *
* * *
# Approach
1. No. of rows = Pattern has 3 rows. We have to print pattern for N rows.
2. No. of cols = The no.of cols in any row is equal to N.
3. What to print = In 1st row, while colNumber<= 2 (N-row), we print " " in every column. Beyond the 2nd col we print "*"
Similarly, in 2nd row, we will print a " " (space) till colNumber<=2(3-2) and beyond the 1st col we print "*"
"""
print("Using while loop")
N = 3
row = 1
while row <= N:
    col = 1
    while col <=N:
        if (col<=(N-row)):
            print(" ", end =' ')
        else:
            print("*", end=' ')
        col+=1
    row+=1
    print()

# Using for loop
print("Using for loop")
N=5
i_count = 0
j_count = 0
for i in range(N):
    for j in range(i+1):
        print("*", end=" ")
        j_count+=1
    i_count+=1
    print()
print(i_count,j_count)
    
