from pygame import Color, draw

class Gizmo():
    def __init__(
            self,
            position=(0,0),
            size=(0,0),
            borderColor=Color(255,255,255),
            borderWidth = 1,
        ):
        self.position = position
        self.size=size
        self.borderColor = borderColor
        self.borderWidth = borderWidth

        self.selStart = (0,0)

    def setEndPoint(self, pos):
        x,y = self.selStart
        w = pos[0]-x
        h = pos[1]-y
        if w < 0:
            w = -w
            x -= w
        if h < 0:
            h = -h
            y -= h

        self.position = (x,y)
        self.size = (w,h)
    
    def setStartPoint(self, pos):
        self.selStart = pos
        self.position = pos
        self.size = (0,0)

    def draw(self, window):
        draw.rect(window, self.borderColor, (*self.position, *self.size), width=self.borderWidth)


