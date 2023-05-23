import csv
import pandas

with open("es_50k.txt") as file:
    lines = file.readlines()

spanish_words = []
for line in lines:
    line = line.strip()
    line = line.split(" ")
    spanish_words.append(line[0])

df = pandas.DataFrame(spanish_words)
df.to_csv("es.csv")
