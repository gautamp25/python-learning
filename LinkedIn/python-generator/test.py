some_word = ['voice','bark','apple',"convention",'crusade','perinnial']
f1 = (item for item in some_word if "i" in item)
f1_el = list(f1)
f2_el = list(f1)
print(f1_el)
print(f2_el)