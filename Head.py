class Head:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def moveX(self, direction):
        self.x += (5 * direction)

    def moveY(self, direction):
        self.y += (5 * direction)

    def getX(self):
        return self.x

    def getY(self):
        return self.y
