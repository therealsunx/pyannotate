from .winelement import WinElement
from pygame import mouse, Color
from pygame import MOUSEBUTTONDOWN

class Button(WinElement):
    def __init__(
            self,
            child,
            onClick=None,
        ):
        WinElement.__init__(self, name="Button")
        self.child = child
        self.onClick = onClick

    def updatePose(self, parentPos, size, offset=(0,0), recalc=False):
        self.child.updatePose(parentPos, size, offset, recalc)

    def render(self):
        self.child.render()

    def draw(self, window):
        self.child.draw(window)

    def handleEvents(self, events):
        ms = mouse.get_pos()
        rect = (*self.child.position,
                self.child.position[0]+self.child.size[0],
                self.child.position[1]+self.child.size[1])
        
        hitt = rect[0]<=ms[0]<=rect[2] and rect[1]<=ms[1]<=rect[3]
        if not hitt: return
        
        for e in events:
            if e.type == MOUSEBUTTONDOWN:
                if self.onClick: self.onClick(self.child)
                break

    def passEvents(self, events):
        self.handleEvents(events)
        self.child.passEvents(events)

