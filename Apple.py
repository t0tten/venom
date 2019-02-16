import random

class Apple:

    def __init__(self, xCord, yCord):
        self.xCord = xCord
        self.yCord = yCord

    def spawn(self,t):
        t.forward(self.xCord)
        t.forward(self.yCord)
        t.dot(20,"red")

    

