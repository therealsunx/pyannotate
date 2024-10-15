from .stack import Stack
from .text import Text
from .image import Image
from .row import Row
from pygame import Color
from pygame import mouse

class Canvas(Stack):
    def __init__(
            self,
            background=None,
            position=(0,0),
            color=Color(20,20,20),
            flex=1.0,
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
        return childs
    
    def handleEvents(self, events):
        self.updateCursor()

    def updateCursor(self):
        curs = mouse.get_pos()
        self.cursor = (curs[0]-self.position[0],
                       curs[1]-self.position[1])


