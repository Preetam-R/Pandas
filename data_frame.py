import pandas as pd

#lets create the dictionaries and convert it into data frame.

data = {
    "name":["Preetu","maanu"],
    "lemons":[7,4]
}

data = pd.DataFrame(data)   #either u can pass dictionary as a argument
print(data)
print("*"*30)
#data frame is the collection of series

s1 = pd.Series([10,20,30,40,50])
s2 = pd.Series([1,2,3,4,5])

si = pd.DataFrame({"C1":s1,"C2":s2})
print(si)

print("*"*30)

#ATTRIBUTES

#  1.SHAPE

print(data.shape)
print(si.shape)
print("*"*30)

#  2.columns

print(data.columns)
print(si.columns)
print("*"*30)

#  3.dtypes

print(data.dtypes)
print(si.dtypes)
print("*"*30)


#you can also have the conditions in the dataframe 
#like,

print(si[si['C1']>30])  #you can use all the relational operators for the conditions
print()


