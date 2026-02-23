#now lets see how to access the dataframe elements
import pandas as pd
#lets take the previous data frame

s1 = pd.Series([10,20,30,40,50])
s2 = pd.Series([1,2,3,4,5])

si = pd.DataFrame({"C1":s1,"C2":s2})
print(si)
print()

# 1.USING LABELS
print("Accessing the elements using the loc")
print(si.loc[3,'C2'])
#in this method (.loc[]) we need to specify the labels of row , column (labels may be integers or strings or anything)


#  2.USING INDEX
print()
print("Accessing the elements using iloc")
print(si.iloc[2,0])

