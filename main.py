import turtle

import pandas as pd

from text_overlay import TextOverlay

text_overlay = TextOverlay()

"""Sets up the screen to reduce white border"""
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(750, 500)

"""Imports the image into the turtle canvas"""
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_50_states = pd.read_csv("50_states.csv")
all_50_states_list = all_50_states.state.to_list()
# print(data)


if len(text_overlay.all_guesses) < len(all_50_states.state):
    game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Guess the State",
                                    prompt="What's another state name?").title()
    if answer_state in all_50_states_list:
        state = all_50_states[all_50_states.state == answer_state]
        # print(state)
        get_x = state.x.iloc[0]
        get_y = state.y.iloc[0]
        text_overlay.pin_answer(state.state.iloc[0], get_x, get_y)

    if answer_state == "Exit":
        print(text_overlay.all_guesses)
        missing_states = []
        # game_is_on = False
        for state in all_50_states_list:
            if state not in text_overlay.all_guesses:
                missing_states.append(state)
        remaining_states_to_guess = pd.DataFrame(missing_states)
        remaining_states_to_guess.to_csv("remaining_states.csv")
        break
    # """Detects the coordinates based on mouse click"""
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinate)

turtle.mainloop()
