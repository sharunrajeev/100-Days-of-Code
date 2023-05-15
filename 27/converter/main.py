import tkinter as tk

window = tk.Tk()
window.title("Miles to KM Converter")
window.minsize(width=100, height=75)
window.config(padx=30, pady=20)

# User entry
miles_entry = tk.Entry(width=10)
miles_entry.grid(column=1, row=0)
miles_entry.focus()

# Labels
label_1 = tk.Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = tk.Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = tk.Label(text="0")
label_3.grid(column=1, row=1)

label_4 = tk.Label(text="Km")
label_4.grid(column=2, row=1)


# Button
def on_submit():
    miles = miles_entry.get()
    kms = float(miles) * 1.609344
    label_3.config(text=f"{kms:.2f}")


button = tk.Button(text="Calculate", command=on_submit)
button.grid(column=1, row=2)

window.mainloop()
