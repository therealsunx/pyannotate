from .stack import Stack
from .text import Text
from .image import Image
from .row import Row
from .gizmo import Gizmo

from pygame import Color, Surface
from pygame import mouse
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION

class Canvas(Stack):
    def __init__(
            self,
            background=None,
            position=(0,0),
            color=Color(20,20,20),
            flex=1.0,
            onSelect = None
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
        self.selMode = False
        self.onSelect = onSelect
    
    def createChilds(self, background=None):
        childs = []
        if background :
            self.background = Image(src=background)
            childs.append(self.background)
        self.selGizmo = Gizmo()
        return childs
    
    def handleEvents(self, events):
        self.updateCursor()
        ms = mouse.get_pos()
        rect = (*self.position,
                self.position[0]+self.size[0],
                self.position[1]+self.size[1])
        
        hitt = rect[0]<=ms[0]<=rect[2] and rect[1]<=ms[1]<=rect[3]
        if hitt: self.updateSelection(events)

    def updateSelection(self, events):
        for e in events:
            if e.type == MOUSEBUTTONDOWN:
                self.selMode = True
                self.selGizmo.setStartPoint(self.cursor)
            if self.selMode and e.type == MOUSEMOTION:
                self.selGizmo.setEndPoint(self.cursor)
            if e.type == MOUSEBUTTONUP:
                if self.onSelect: self.onSelect(self.getSelection())
                self.selMode = False
    
    def getSelection(self):
        if not self.selMode: return (0,0,0,0)
        return (*self.selGizmo.position, *self.selGizmo.size)

    def updateCursor(self):
        curs = mouse.get_pos()
        self.cursor = (curs[0]-self.position[0],
                       curs[1]-self.position[1])

    def render(self):
        if not self.surface:
            self.surface = Surface(self.size)
            self.surface.convert_alpha()
        self.surface.fill(self.color)
        for c in self.children:
            c.draw(self.surface)

        if self.selMode: self.selGizmo.draw(self.surface)

