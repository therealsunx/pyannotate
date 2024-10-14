from .winelement import WinElement
from pygame import Surface, Color

class Stack(WinElement):
    def __init__(
            self,
            children,
            name="STACK",
            flex=1,
            padding=(0,0),
            color=Color(0,0,0,0),
            position=(0,0),
            surface=None
        ):
        WinElement.__init__(
                self,
                name, flex, color,
                position=position,
                surface=surface
            )
        self.padding = padding
        self.children = children

    def updatePose(self, parentPos, size, offset=(0,0), recalc=False):
        self.position = (parentPos[0]+offset[0], parentPos[1]+offset[1])
        self.offset = offset
        self.size = size
        if not recalc: return
        
        for c in self.children:
            # cpos = (self.position[0]+c.position[0], self.position[1]+c.position[1])
            c.updatePose(self.position, self.size, c.position, recalc)

    def render(self):
        if not self.surface:
            self.surface = Surface(self.size)
            self.surface.convert_alpha()
        self.surface.fill(self.color)
        for c in self.children:
            c.draw(self.surface)

    def passEvents(self, events):
        self.handleEvents(events)
        for c in self.children:
            c.passEvents(events)

