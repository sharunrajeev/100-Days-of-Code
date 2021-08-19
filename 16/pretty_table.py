from prettytable import PrettyTable

table = PrettyTable()

# table.field_names = ['Pokemon Name', 'Type']
# table.add_row(['Pikachu', 'Electric'])
# table.add_row(['Squirtle', 'Water'])
# table.add_row(['Charmander', 'Fire'])

# Alternate method
# Class method
table.add_column('Pokemon name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])

# Class attribute
table.align = 'l'
print(table)
