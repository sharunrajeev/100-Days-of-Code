PLACEHOLDER = '[Name]'

with open('./Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    to_change_lines = letter_file.read()
    to_change_lines = to_change_lines.splitlines()
    for name in names:
        name = name.strip("\n")
        to_change_lines[0] = to_change_lines[0].replace(PLACEHOLDER, name)
        to_write = '\n'.join(to_change_lines)
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as result_file:
            result_file.write(to_write)

print("Mails created!")
