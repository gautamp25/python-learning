# compress string
# aabbccddeeee = a2b2c2d2e4

# input-aabbccaaaafffeiii
# output-a2b2c3a4f3e1i3

# By using for loop

s = "aabbcdddii"
def cmp_str(s):
    str_len = len(s)
    # print(str_len)
    new_str = ''
    count = 1
    for i in range(str_len-1):
        if s[i] == s[i+1]:
            print("1",s[i])
            print("2",s[i+1])
            count += 1
        else:
            new_str = new_str + s[i] + str(count)
            count = 1
        # print(count)
    new_str = new_str + s[str_len-1] + str(count)
       
    return new_str

print(cmp_str(s))

    
# by while loop
def cmp_str1(s):
    n = len(s)
    i = 0
    new_str = ""
    while(i<n-1):
        count = 1
        while(i<n-1 and s[i]==s[i+1]):
            count += 1
            i += 1
        i+=1
        new_str = new_str + s[i-1]+str(count)
    return new_str

print(cmp_str1(s))
