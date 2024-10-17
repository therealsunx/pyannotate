from .winelement import WinElement
from pygame import mouse, Color, draw
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP

class Button(WinElement):
    def __init__(
            self,
            child,
            id=0,
            flex=1,
            onClick=None,
        ):
        WinElement.__init__(self, name="Button", id=id, flex=flex)
        self.child = child
        self.onClick = onClick
        self.clicked = False

    def updatePose(self, parentPos, size, offset=(0,0), recalc=False):
        self.child.updatePose(parentPos, size, offset, recalc)

    def render(self):
        self.child.render()
    
    def draw(self, window, highlight=False):
        self.child.draw(window, self.clicked or highlight)

    def handleEvents(self, events):
        ms = mouse.get_pos()
        rect = (*self.child.position,
                self.child.position[0]+self.child.size[0],
                self.child.position[1]+self.child.size[1])
        
        hitt = rect[0]<=ms[0]<=rect[2] and rect[1]<=ms[1]<=rect[3]
        if not hitt: return
        
        for e in events:
            if e.type == MOUSEBUTTONDOWN:
                self.clicked = True
                if self.onClick: self.onClick(self)
                break
            if e.type == MOUSEBUTTONUP:
                self.clicked = False

    def passEvents(self, events):
        self.handleEvents(events)
        self.child.passEvents(events)

