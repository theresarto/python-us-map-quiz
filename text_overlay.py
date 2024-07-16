from turtle import Turtle

REG_FONT = ("Arial", 12, "normal")
ALIGN = "Center"


class TextOverlay:
    def __init__(self):
        self.all_guesses = []

    def pin_answer(self,  state, x, y):
        pin = Turtle()
        pin.penup()
        pin.ht()
        pin.color("black")
        pin.speed("fastest")

        pin.goto(x, y)
        pin.write(state, align=ALIGN, font=REG_FONT)

        self.all_guesses.append(pin)



