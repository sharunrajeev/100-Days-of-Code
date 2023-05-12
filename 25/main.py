# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data["temp"])

# Convert to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# Convert to list
# data_list = data["temp"].to_list()

# To get average
# print("Average = ", sum(data_list) / len(data_list))
# print(data["temp"].mean())

# To get max
# print(data["temp"].max())

# Get data from column
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])

# Challenge
# Row with max temperature
# print(data[data.temp == data.temp.max()])

# Challenge
# monday = data[data.day == "Monday"]
# print((((monday.temp)*9)/5)+32)

# Create a dataframe from scratch
students_dict = {
    "students": ["Sharun", "Shravan", "Adish"],
    "marks": [75, 90, 85]
}
student_df = pd.DataFrame(students_dict)
student_df.to_csv("new_data.csv")
