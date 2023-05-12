# Create a new pandas dataframe from the CSV data which counts the squirrels with specific fur colour

import pandas as pd

csv_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(csv_data[csv_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(csv_data[csv_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(csv_data[csv_data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

new_df = pd.DataFrame(squirrel_dict)
new_df.to_csv("squirrel_count.csv")