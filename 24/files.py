# One way to read
# text_file = open('text.txt')
# print(text_file.read())
# text_file.close()

# Read using "with" keyword
with open("text.txt") as text_file:
    print(text_file.read())

# Write into the file
# If file does not exist then file gets created
with open("text.txt", "w") as text_file:
    text_file.write("This is a new file")

# Append to the file
with open("text.txt", mode="a") as text_file:
    text_file.write("New text is added")
