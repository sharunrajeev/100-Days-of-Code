import tkinter as tk

window = tk.Tk()
window.title("First GUI Program")
window.minsize(width=400, height=300)

# Label
my_label = tk.Label(text="This is a text")
my_label.pack()


# Button
def handle_click():
    my_label["text"] = user_entry.get()


my_button = tk.Button(text="Click me", command=handle_click)
my_button.pack()

# Entry (User Input Bar)
user_entry = tk.Entry(width=50)
user_entry.insert(index=0, string="Enter some text to change the label.")
user_entry.pack()

# Text (Text Box)
text_box = tk.Text(height=5, width=50)
text_box.focus()
text_box.insert(index=0.0, chars="Example of multiline text entry")
print(text_box.get(0.0))
text_box.pack()

window.mainloop()
