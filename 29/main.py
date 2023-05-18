# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
BG = "#fefae0"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data_to_file():
    website_data, email_data, password_data = website_entry.get(), email_entry.get(), password_entry.get()
    if not website_data or not email_data or not password_data:
        messagebox.askretrycancel(title="Oops!", message=f"Please don't leave any empty fields!")
    else:
        confirmation = messagebox.askokcancel(title=website_data,
                                              message=f"These are the details entered:\nEmail/Username: {email_data}\nPassword: {password_data}\nIs it okay to save?")
        if confirmation:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website_data} | {email_data} | {password_data}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "sharunpublic@gmail.com")
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=50, pady=50, bg=BG)

canvas = Canvas(width=200, height=200, bg=BG, highlightthickness=0)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website URL", bg=BG)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username", bg=BG)
email_label.grid(column=0, row=2)
password_label = Label(text="Password", bg=BG)
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=51)
website_entry.focus()
website_entry.grid(sticky='W', column=1, row=1, columnspan=2)
email_entry = Entry(width=51)
email_entry.insert(index=0, string="sharunpublic@gmail.com")
email_entry.grid(sticky='W', column=1, row=2, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(sticky='W', column=1, row=3)

# Buttons
generate_pw_button = Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(sticky='W', column=2, row=3)
add_button = Button(text="Add", width=43, command=save_data_to_file)
add_button.grid(sticky='W', column=1, row=4, columnspan=2)

window.mainloop()
