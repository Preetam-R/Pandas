#  NOW LETS SEE THE HOW DOES THE DATA AGGREGATION PROCESS

import pandas as pd

data = pd.DataFrame({"Name":["a","b","a","b","c"],"Scores":[10,20,30,40,50]})
print(data)
print()

grouped = data.groupby('Name')
summ = grouped.sum()
print(summ)  #printing sum of groupby elements
print()

print("printing mean\n")
meann = grouped.mean()
print(meann)
#like this we can also print min() max() and mean()

gp = grouped.max()
print(gp)

#pivot table

#pivot table is tool in which the data are computed by taking the mean of the elements 
# lets understand by the example

#lets consider the dataframe "data"
#and implement in to pivot table 

pt = data.pivot_table(values = 'Scores', index = 'Name')
print("printing pivot table\n")
print(pt)  
print()

#  CROSS TAB

#is used to summarize the relationship between two or more categorical variables in the form of a table

cr = pd.crosstab(data['Name'],data['Scores'])
print(cr)


#   joining append merging


s1 = pd.Series(data=['A','B','A','B','C'])
s2 = pd.Series(data=[11,22,33,44,55])
data2 = pd.DataFrame({'Name':s1,
'Lemon':s2})
print(data2)

s1 = pd.Series(data=['A','B','A','B','C'])
s2 = pd.Series(data=[10,20,30,40,50])
data1 = pd.DataFrame({'Name':s1,
'Lemonades':s2})
print(data1)


con = pd.concat([data1, data2])
print(con)
print()

#merging 
#in merging we dont see the NaN value unlike concat and will merge on basis of one common field
mer = pd.merge(data1, data2, on='Name')
print(mer)

# Join on Index:
#data1.join(data2.set_index('Name'), on='Name')

#these do the same task as merge
print(data.plot(kind = 'scatter',x='Name',y='Name'))