# Sort students by marks in descending order.


import pandas as pd

students = pd.DataFrame({
    "Name":["A","B","C","D"],
    "Marks":[85,40,52,30]
})

print(students)

print("in descending order")
print(students.sort_values(by ='Marks',ascending = False))