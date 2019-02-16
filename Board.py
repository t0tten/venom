from turtle import Turtle
from Apple import *
import random

class Board:

    def __init__(self):
        self.data = []
        t = Turtle()
        t.screen.title("Venom")
        t.screen.bgcolor('black')
        t.hideturtle()
        t.penup()
        
        x = random.randint(-1000,1000)
        y = random.randint(-300,300)
        a = Apple(x,y)
        a.spawn(t)

        t.screen.exitonclick()
        t.screen.mainloop()

