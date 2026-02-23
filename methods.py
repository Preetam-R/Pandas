#lets see the methiods used in the pandas 
import pandas as pd

s1 = pd.Series([10,20,30,40,50,60,70,80,90,100])
s2 = pd.Series([1,2,3,4,5,6,7,8,9,10])

si = pd.DataFrame({"C1":s1,"C2":s2})
print(si)
print()

#  1.head

print("Head method")
print(si.head())
print()

#  2.tail method
print("tail method")
print(si.tail())
print()

#  3.count method

print("counting the no. elements in the dataframe.")
print(si.count())
print()

#  4.info method
#info methods tells you everything about the data

print("Printing the info of the dataframe.")
print(si.info())
print()

#  5.describe method
#  count: Number of non-null observations.
# mean: The average value.
# std: The standard deviation (measure of data spread).
# min: The minimum value.
# 25%, 50%, 75%: Percentiles (the 50th percentile is the median).
# max: The maximum value 

print("Printing decribe method")
print(si.describe())
print()

#  6. sort_values method is used to sort the values 
#  7. isnull method is used to check the null values in the dataframe

