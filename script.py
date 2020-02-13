#!/usr/bin/env/python3


import pandas as pd
xl_file = input("Enter File name without Extension:==> ")
data = pd.read_excel(xl_file+".xlsx")
#print(data)
#print(data.head())
#print("After dataframe")
#print(data['Description'])
#print("After 8")
#row1 = data.iloc['0']
dict = data.to_dict()
#print(dict)

#print(data.drop(["unnamed "]),axis=1)
'''
for i in data:
    print(i)
    print(data[i])
'''
row, col = data.shape
#print(row,col)
#print(len(dict.get("Refernce_Code","Code label")))
from collections import defaultdict
dictRes=defaultdict(list)
lisres=[]
for d in dict.values():
    lisres.append(d)
#print(lisres)

for dd in (lisres):
    #print(dd)
    for key, value in dd.items():
        dictRes[key].append(value)
#print(dictRes)
userinput = input("Enter yes to start updating and no to abort(yes/no):==>")
if(userinput == 'yes'):
    for res in dictRes.values():
        print(res)
    print("Update Successful...")
else:
    print("Aborted, nothing is updated...")




'''
for items in dict.values():
    for keys in items:
        if keys == 0:
            list1.append(items[keys])
        elif keys == 1:
            list2.append(items[keys])
        elif keys == 2:
            list3.append(items[keys])
print(list1)
print(list2)
print(list3)
'''