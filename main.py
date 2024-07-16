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

"""Reads the csv file"""
data = pd.read_csv("50_states.csv")
# print(data)





if len(text_overlay.all_guesses) < len(data.state):
    game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?")
    if answer_state.title() in data.state.values:
        state = data[data.state == answer_state]
        # print(state)
        get_x = state.x.iloc[0]
        get_y = state.y.iloc[0]
        text_overlay.pin_answer(state.state.iloc[0], get_x, get_y)


# """Detects the coordinates based on mouse click"""
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinate)

turtle.mainloop()
