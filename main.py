import turtle
import pandas
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

image = resource_path("blank_states_img.gif")

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(resource_path("50_states.csv"))

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} States Correct",
        prompt="Guess another state"
    )

    if not answer_state:
        break

    answer_state = answer_state.title()

    if answer_state in all_states and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

        guessed_states.append(answer_state)

os.makedirs("evaluation", exist_ok=True)

evaluation = pandas.DataFrame({
    "State": all_states,
    "Status": ["Guessed" if state in guessed_states else "Missed" for state in all_states]
})

evaluation.to_csv("evaluation/analysis.csv")

screen.exitonclick()