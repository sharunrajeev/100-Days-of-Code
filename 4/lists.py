# Lists

lists = ["one", "two", 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# In usual order
for i in range(0, len(lists)):
    print(lists[i])
print("---------")

# In reversed order
for i in range(0, len(lists)):
    print(lists[-i])

# Adding single element to list
lists.append("eleven")

# Adding many elements to list
lists.extend(["twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"])