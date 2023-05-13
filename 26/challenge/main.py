import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary from this data
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

user_input = input("Enter a word: ")
nato_words = [nato_dict[letter.upper()] for letter in user_input]

print(nato_words)
