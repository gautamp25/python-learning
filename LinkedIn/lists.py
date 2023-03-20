# #list comprehensions

# myList = [1,2,3,4]
# print([2*item for item in myList])

# # List comprehension with filters
# my_list = list(range(100))
# filtered_list = [i for i in my_list if i%10==0]
# print(filtered_list)

# #List comprehension with functions

# my_string = "My name is Gautam. I live in Pune"
# def cleanWord(word):
#     return word.replace('.','').lower()

# print([cleanWord(word) for word in my_string.split()])


# # Nestead List comprehension
# print([[cleanWord(word) for word in sentence.split()] for sentence in my_string.split('.') ])

def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar!= char:
            encodedList.append((prevChar,count))
            count = 0
        prevChar = char
        count+=1
        
    encodedList.append((prevChar,count))
    return encodedList

print(encodeString('AABBBCC'))

myLst= [2]
for i in range(3,10):
    count = 0
    print(i)
    for num in range(2,(i//2+1)):
        if i%num ==0:
            count+=1
            break
            
    if count==0 and i!=1:
        myLst.append(i)