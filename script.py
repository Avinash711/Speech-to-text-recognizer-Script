import pandas as pd
xl_file = input("Enter File name without Extension:==> ")
data = pd.read_excel(xl_file+".xlsx")
print(data)
#print(data.head())
#print("After dataframe")
#print(data['Description'])
print("After 8")
#row1 = data.iloc['0']
dict = data.to_dict()
print(dict)

#print(data.drop(["unnamed "]),axis=1)
'''
for i in data:
    print(i)
    print(data[i])
'''
row, col = data.shape
print(row,col)
print(len(dict.get("Refernce_Code","Code label")))
list1=[]
list2=[]
list3=[]
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