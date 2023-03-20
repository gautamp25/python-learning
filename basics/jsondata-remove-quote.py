"""import glob
import json
searchjson = r'D:\DataStructureAndAlgorithm\basics\pofg_xrf_data_trial.json'
data = json.loads(open(searchjson).read())
apilist = []
thelist = []
for value in data["pofg_xrf_data"]:
    # print(value['api_no_10'])
    tempdict = {}
    # if value['api_no_10'] not in apilist:
    if len(value['api_no_10'])>0:
       
        thelist.append(tempdict)

with open('basics/pofg_xrf_data_trial.json', "w") as jsonFile:
    json.dump(thelist, jsonFile, indent=4)
# with open(r'D:\python\json read and search\apilist2.txt', 'w') as file:
#     file.write(str(apilist))
# print(value)
print('done')
"""

import json
import random

# in_file_path=r'D:/DataStructureAndAlgorithm/basics/testjson.json' # Change me!
# n = str(random. randint(0,10))
# print(n)
# with open(in_file_path,'r') as in_json_file:

#     # Read the file and convert it to a dictionary
#     json_obj_list = json.load(in_json_file)
#     print(type(json_obj_list))

#     for json_obj in json_obj_list['pofg_xrf_data']:
#         filename=json_obj['wellId']+'.json'

#         with open(filename, 'w') as out_json_file:
#             # Save each obj to their respective filepath
#             # with pretty formatting thanks to `indent=4`
#             json.dump(json_obj, out_json_file, indent=4)

import os
import json
#you need to add you path here
with open(os.path.join("D:/DataStructureAndAlgorithm/basics/", "testjson.json"), "r",encoding='utf-8') as f1:
    ll = [json.loads(line.strip()) for line in f1.readlines()]

    #this is the total length size of the json file
    print(len(ll))

    #in here 2000 means we getting splits of 2000 tweets
    #you can define your own size of split according to your need
    size_of_the_split=2000
    total = len(ll) // size_of_the_split

    #in here you will get the Number of splits
    print(total+1)

    # for i in range(total+1):
    #     json.dump(ll[i * size_of_the_split:(i + 1) * size_of_the_split], open(
    #         "D:/DataStructureAndAlgorithm/basics/new-folder/data_split" + str(i+1) + ".json", 'w',
    #         encoding='utf8'), ensure_ascii=False, indent=True)