"""
Dict comprehension-
    Output- dictionary key-value pair
    Input- Loop iteration needed for computation
    Conditional- needed only if computation is required



"""

sal_data_keys = ["Austin","Portland","Dallas","Atlanta"]
sal_data_values = [91185,110123,89123,12000]
sal_info ={}
print("Creating dictionary without using comprehension")
for key, value in zip(sal_data_keys,sal_data_values):
    sal_info[key] = value
print(sal_info)
sal_info.clear()

print("Creating dictionary using dict comprehension")
my_dict = {key:value for key,value in zip(sal_data_keys,sal_data_values)}
print(my_dict)
sal_info = {sal_data_keys[indx]:sal_data_values[indx]  for indx in range(0,len(sal_data_keys))}
print(sal_info)
for k in sal_info.items():
    print(k,print(type(k)))

sal_100k = {k:v for k,v in sal_info.items() if v>100000}
print(sal_100k)