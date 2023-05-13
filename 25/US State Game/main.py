import turtle
import pandas as pd

csv_data = pd.read_csv('50_states.csv')


def get_state_data(user_input):
    return csv_data[csv_data["state"] == user_input]


screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

chances = 0
guessed_states = []
all_states = csv_data.state.to_list()
while chances < 50:
    answer_state = screen.textinput(title=f"Correct Guess ({len(guessed_states)}/50)", prompt="What's another state name?").title()
    state_data = get_state_data(answer_state)
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if not state_data.empty:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)
    chances += 1

