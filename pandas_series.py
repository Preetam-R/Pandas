#firstly import pandas library and this will be sa,e steps for everytime

import pandas as pd

#series is one complete list where the elements are passed as comma separated

#for example

sales = pd.Series([9,3,1,6])
print(sales)  #this is the series
#above we have created the series 
#-----------------------------------------------------------------------------------------------------------
#now lets know how to access the element from the series

#There are two methods to access the elements 1.indexing 2.slicing

#lets see the indexing first 

#lets consider above series
print("-"*30)
print("INDEXING")
print(sales[1])

#slicing
print("-"*30)
print("SLICING")
print(sales[0:2])

print("-"*30)

#-----------------------------------------------------------------------------------------------------------
#ATTRIBUTES

#at the same time you can also check the range of your Series
#index
print(sales.index)
print("-"*30)

#values
print(sales.values)
 
 #dtype
print(sales.dtype)

print("-"*30)

#sales.head is used to see the first 5(By Default) elements of the series
#even you can pass the parameters like sales.head(2)... it will show first 2 elements

print(sales.head)
print(sales.head(2))
print("-"*30)

#like the same way to get last elements of the series we use sales.tail (by default-5, parameters can be passed like head)


#sales.sort_values
#this is used to sort the series in order
print(sales.sort_values())
print("-"*30)

#sales.count()
#this tells how much elements are there in series

print("elements is the series are:",sales.count())
print("-"*30)

#-----------------------------------------------------------------------------------------------------------

#OPERATIONS
#we can use vectorisation on series
#like sales + 1 will return the series with adding the 1 to every element and works on all arithematic operations

