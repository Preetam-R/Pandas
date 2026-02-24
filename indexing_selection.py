import pandas as pd

#you can also have the custom indexing column of your choice

#for that lets make the data frame first

p = ["a","b","c","d","e"]
m = [10,20,30,40,50]

data = pd.DataFrame({"Sl.":p,"Beta":m})
print(data)
print()
#now the dataframe is constructed but i need column alpha as the indexing
#for that we can do,    *.set_index('coloumn_name')

print("After setting the 'Sl.' as the index.\n")
data.set_index('Sl.',inplace = True)
print(data)
print()
#to restore the index you can reset by executing reset method
data.reset_index(inplace=True)
print(data)
print("-"*40)

#you can also do multi indexing 
m_index = pd.DataFrame({
    'Name':['a','a','b','b'],
    'qant':[10,30,20,40],
    'park':[1,2,3,4]
}).set_index(['Name','park'])
print(m_index)
print()


#selection
print(m_index[m_index['qant']>20])
print()

#query method          #query method is very easy to understand unlike selection method
print("printing query method")
print(m_index.query('qant >= 20'))
