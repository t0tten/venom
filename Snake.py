from Head import Head
from Body import Body
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Snake:
    def __init__(self):
        self.direction = Direction.RIGHT
        self.head = Head(0, 0)
        self.body = None
        self.spriteDimension = 5

    def moveBody(self):
        tmpX = self.head.getX()
        tmpY = self.head.getY()

        for bodyPart in self.body:
            prevBodyX = bodyPart.getX()
            prevBodyY = bodyPart.getY()

            bodyPart.setX(tmpX)
            bodyPart.setY(tmpY)

            tmpX = prevBodyX
            tmpY = prevBodyY

    def update(self):
        self.moveBody()

        if direction is Direction.UP:
            self.head.moveX(-1)
        elif direction is Direction.DOWN: 
            self.head.moveX(1)
        elif direction is Direction.LEFT:
            self.head.moveY(-1)
        elif direction is Direction.RIGHT: 
            self.head.moveY(1)

        self.checkCollision()

    def addBody(self, x, y):
        if direction is Direction.UP:
            self.body.append(Body(x + self.spriteDimension, y))
        elif direction is Direction.DOWN:
            self.body.append(Body(x - self.spriteDimension, y))
        elif direction is Direction.LEFT:
            self.body.append(Body(x, y + self.spriteDimension))
        elif direction is Direction.RIGHT:
            self.body.append(Body(x, y - self.spriteDimension))

    def checkCollision(self, x, y):
        pass

    def setDirection(self, direction):
        self.direction = direction 
