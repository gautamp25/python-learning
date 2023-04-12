name= 'gautam'
print(name[::-1])
v=''
lst= [1,2,3,4,5]
def rev(lst):
    if not lst:
        return []
    return(lst[-1]+rev(lst[:-1]))
print(rev([1,2,3,4,5]))