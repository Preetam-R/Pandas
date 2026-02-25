import pandas as pd
#HANDLING MISSING DATA

#lets take the series

sd = pd.Series([5,None,9])
print(sd)
print()

#now i can drop the NaN data
k = sd.dropna()
print(k)

#or i can fill the NaN with any number (commonly used 0)
sd = sd.fillna(0)
print(sd)

#  REMOVING DUPLICATE ITEMS

lt = [1,2,1,4,5]
p = [1,3,1,6,7]
data = pd.DataFrame({"c1":lt,"c2":p})
print(data)

#to remove the duplicate data
du = data.drop_duplicates()
print(du)

#  REPLACE

re = data.replace(1,69)
print(re)