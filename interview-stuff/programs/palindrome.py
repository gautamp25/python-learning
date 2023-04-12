# Palindrome Number

# A. By using split method

from tkinter import N


def palindrome(s):
    temp = s[::-1]
    if temp == s:
        print("Yes!! It's palindrome")
    else:
        print("No!! It's not Palindome")

s = "NITIN"
palindrome(s)

# By using indexing/using loop
s = "rrrrrra"
# by adding the reverse of the string to it:
s = s + s[::-1]
print(s)
# by adding characters to one end of the string until it becomes a palindrome:
s = "rrrrrra"
while s != s[::-1]:
    s = s[0] + s
print(s)
rrrrrrra

def palindrome2(p):
    p_len = len(p)
    for i in range(p_len):
        if p[i] != p[p_len-i-1]:
            print(p[i])
            return False
    return True

p = "1nitin1"
q= "rrrrrra"
q= "arrrrrra"

print(palindrome2(q))

# By using in-build function- reversed & join
def palindrome3(a):
    # rever = reversed(a)
    # print(rever)
    temp_rev = ''.join(reversed(a))
    # print(temp_rev)
    if a == temp_rev:
        return True
    else:
        return False

obj = "NITIN1"
print(palindrome3(obj))

# By using while 
def palindrome4(s):
    s_len = len(s)
    first = 0
    last = s_len-1
    while(first<last):
        if s[first] == s[last]:
            first += 1 #first = first+1
            last -= 1 #last = last-1
        else:
            return False
    return True

s = "malayalam"
print("4th")
print(palindrome4(s))



# By recursive function
def isPalindrome(s):
    s_len = len(s)
    if s_len<2:
        return True
    elif s[0] == s[s_len-1]:
        # print("HI")
        # print(s)
        return isPalindrome(s[1:s_len-1])
    else:
        return False

s = "malayalam"
print("---Palindrome string Using recursion---")
print(isPalindrome(s))



# Palindrome number using while loop 
def check_palindrome(n):
    temp = n
    rev_n = 0
    while(temp>0):
        # print("TEMP",temp)
        digit = temp % 10 # reminder value
        # print("REM",146%10)
        # print("Before",rev_n)
        rev_n = rev_n * 10 + digit # 0*10+1 = 1
        # print("After",rev_n)
        temp = temp//10 #145

        # print('---',temp)

    if n == rev_n:
        return True
    else:
        return False

num = 12345654321
print("----Using while loop---")
print(check_palindrome(num))

# Palindrome number using recursion

def rec(n,temp):
    if n==0:
        return temp
    temp = (temp *10) + (n % 10)
    # print(temp)
    return rec(n//10,temp)

print("----Palindrome Number Using recursive function---")
num = 12345654321
ans = rec(num,0)
if ans == num:
    print("Yes")
else:
    print("No")



