# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial Rounded MT Bold"
FONT_SIZE = 35
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
checkmarks = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer, checkmarks
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    if reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer, checkmarks
    minutes = floor(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 60)
    else:
        start_timer()
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            checkmarks += '✔️'
        check_label.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)
check_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, "bold"))
check_label.grid(column=1, row=3)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
# First two arguments denote the position of the element (x,y)
canvas.create_image(100, 111, image=photo_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, FONT_SIZE, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", padx=10, pady=4, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", padx=10, pady=4, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
