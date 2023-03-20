a = {}
b = {1}
c=''
d= None
print(type(c),type(d))
data = {"inv":'123', 'items':[{'amt': 120,'rate':50}] }
for key,val in data.items():
    print(val)
# def my_fun(ocr_rate=None):
#     print('rate=',ocr_rate)
#     # pass

# ocr_rate = None
# ocr_item= data['items']
# for item in ocr_item:
#     if 'rate' in item:
#         ocr_rate = item['rate']
#         my_fun(ocr_rate)

#     else:
#         my_fun(ocr_rate)
