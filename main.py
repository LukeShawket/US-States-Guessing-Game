import csv
import pandas
import turtle

screen = turtle.Screen()
screen.title("US States")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

states_data = pandas.read_csv("50_states.csv")
state_list = states_data["state"].to_list()
guessed_states = []

is_game_started = True


def write_state_name(pos_x, pos_y, content):
    t_text = turtle.Turtle()
    t_text.penup()
    t_text.speed("fastest")
    t_text.hideturtle()
    t_text.color("black")
    t_text.goto((pos_x, pos_y))
    t_text.pendown()
    t_text.write(content)

while is_game_started:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="What's the next state's name?")

    if answer in state_list:
        guessed_state = states_data[states_data.state == answer]
        x = guessed_state["x"].values[0]
        y = guessed_state["y"].item()
        write_state_name(x, y, answer)
        guessed_states.append(answer)
    else:
        pass

    if answer == "quit":
        is_game_started = False

turtle.mainloop()