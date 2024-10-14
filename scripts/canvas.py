from .winelements import *
from pygame import Color
from pygame import mouse

class Canvas(Stack):
    def __init__(
            self,
            background=None,
            position=(0,0),
            color=Color(20,20,20),
            flex=1,
        ):
        Stack.__init__(
                self,
                children=self.createChilds(background),
                name="Canvas",
                flex=flex,
                position=position,
                color=color
            )
        self.cursor = (0,0)
    
    def createChilds(self, background=None):
        childs = []
        if background :
            self.background = Image(src=background)
            childs.append(self.background)
        self.cursorText = Text(
                text="x:0, y:0",
                position=(0,0),
                fontSize=16,
                color=Color(0,0,0,0)
            )
        childs.append(self.cursorText)
        return childs
    
    def handleEvents(self, events):
        self.updateCursor()

    def updateCursor(self):
        self.cursor = mouse.get_pos()
        self.cursor = (self.cursor[0]-self.position[0],
                       self.cursor[1]-self.position[1])
        self.cursorText.text = f"x:{self.cursor[0]}, y:{self.cursor[1]}"
        # self.cursorText.position = self.cursor
        self.cursorText.setPosition((self.cursor[0], self.cursor[1]-16))

