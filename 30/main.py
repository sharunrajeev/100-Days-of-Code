try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Works!")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed")
