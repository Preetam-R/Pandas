import pandas as pd
#now lets see how to read and write in CSV files


data = pd.DataFrame({
    'sl.':[1,2,3,4,5],
    'Name':['Preetu','Maanu','Kitty','sinchan','chaaru'],
    'marks':[95,99,89,85,80]
}).set_index('sl.')
print(data)

result = data.to_csv('result.csv')
print()
print("loading the csv file.......")
analysis = pd.read_csv('result.csv')
print(analysis)


#you can also create the dataframe like

listt = [[1, 2, 100], [2, 4, 100], [3, 8, 100]]
pl = pd.DataFrame(listt, columns=['x', 'y', 'z'])
print(pl)