# Select students who scored more than 80 marks.

# Name   Marks
# A      85
# B      60
# C      92
# D      70
import pandas as pd
students = pd.DataFrame({
    "Name":["A","B","C","D"],
    "Marks":[85,60,92,70]
})

print(students)

print("\nthe students who got more than 80 marks are:")
print(students.query('Marks>80'))