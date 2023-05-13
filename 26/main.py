from random import randint
import pandas as pd

students = ['Sharun', 'Shravan', 'Adish', 'Nishitha']
student_scores = {student: randint(1, 100) for student in students}
passed_students = {student: score for (student, score) in student_scores.items() if score > 50}

df = pd.DataFrame(student_scores, index=[0])
# Loop through a dataframe
# for (key, value) in df.items():
#     print(key, value)

# Loop through the rows
# for (index, row) in df.iterrows():
#     print(row)

# To get the data in the row data
# row.column_name
