class Position:
    #TODO : remove getters and setters
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDirection(self):
        return self.direction

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
    
    def setDirection(self, direction):
        self.direction = direction
    
    def is_same_position(pos1, pos2):
        return pos1.getX() == pos2.getX() and pos1.getY() == pos2.getY() 
    
    def is_vertical(pos):
        return pos.getDirection() == config.NORTH or pos.getDirection() == config.SOUTH