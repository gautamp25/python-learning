
"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
 

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.


def splitStr(mystr):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    strlen = len(mystr) # o(1)
    mid = int(strlen/2)
    a = mystr[0:mid]
    b = mystr[mid:]
    print(a,b)
    a_count = 0
    b_count = 0
    for i in a:
        if i in vowels:
            a_count+=1
    for j in b:
        if j in vowels:
            b_count+=1
    if a_count == b_count:
        return True
    else:
        return False 






print(splitStr("&o1234gsot"))

# List of test cases
#1. 
#2.len > 0
#3. len is even
O(n)+ o(m)
O(n+m) 


"""