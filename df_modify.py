import pandas as pd

#ADDING, UPDATE, DELETE

s1 = pd.Series([10,20,30,40,50])
s2 = pd.Series([1,2,3,4,5])

si = pd.DataFrame({"C1":s1,"C2":s2})
print(si)
print()

#ADDING the columns 
si['tips'] = [10,9,8,7,6]
print(si)
print()

#*************************************************************************************
#if you wanna delete then there is two methods
#  *del

# del si['tips']
# print(si)

#  *drop method

# si = si.drop(columns = ['tips'])
# print(si)

#*************************************************************************************

#UPDATING
si.loc[si['C1']== 30] = 143
print(si)
print()

#RENAMING
si = si.rename(columns = {'C1':'Column1'})
print(si)
