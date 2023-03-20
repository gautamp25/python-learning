import glob
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
        apilist.append(value['api_no_10'])
        tempdict["vendor"]= value['vendor']
        tempdict["wellId"]= value['api_no_10']
        tempdict["sample_type"]= value["sample_type"]
        tempdict["depth"]= value["depth"]
        tempdict["raw_name"]= value["raw_name"]
        tempdict["na_pct"]= value["na_pct"]
        tempdict["mg_pct"]= value["mg_pct"]
        tempdict["al_pct"]= value["al_pct"]
        tempdict["si_pct"]= value["si_pct"]
        tempdict["p_pct"]= value["p_pct"]
        tempdict["s_pct"]= value["s_pct"]
        tempdict["k_pct"]= value["k_pct"]
        tempdict["ca_pct"]= value["ca_pct"]
        tempdict["ti_pct"]= value["ti_pct"]
        tempdict["mn_ppm"]= value["mn_ppm"]
        tempdict["fe_pct"]= value["fe_pct"]
        tempdict["ba_ppm"]= value["ba_ppm"]
        tempdict["v_ppm"]= value["v_ppm"]
        tempdict["cr_ppm"]= value["cr_ppm"]
        tempdict["co_ppm"]= value["co_ppm"]
        tempdict["ni_ppm"]= value["ni_ppm"]
        tempdict["cu_ppm"]= value["cu_ppm"]
        tempdict["zn_ppm"]= value["zn_ppm"]
        tempdict["ga_ppm"]= value["ga_ppm"]
        tempdict["as_ppm"]= value["as_ppm"]
        tempdict["pb_ppm"]= value["pb_ppm"]
        tempdict["se_ppm"]= value["se_ppm"]
        tempdict["th_ppm"]= value["th_ppm"]
        tempdict["rb_ppm"]= value["rb_ppm"]
        tempdict["u_ppm"]= value["u_ppm"]
        tempdict["sr_ppm"]= value["sr_ppm"]
        tempdict["y_ppm"]= value["y_ppm"]
        tempdict["zr_ppm"]= value["zr_ppm"]
        tempdict["nb_ppm"]= value["nb_ppm"]
        tempdict["mo_ppm"]= value["mo_ppm"]
        tempdict["u_optimized_ppm"]= value["u_optimized_ppm"]
        tempdict['isActive'] = True
        tempdict['createdAt'] = 'new Date()'
        tempdict['updatedAt'] = 'new Date()'
        thelist.append(tempdict)

with open('basics/pofg_xrf_data_trial.json', "w") as jsonFile:
    json.dump(thelist, jsonFile, indent=4)
# with open(r'D:\python\json read and search\apilist2.txt', 'w') as file:
#     file.write(str(apilist))
# print(value)
print('done')