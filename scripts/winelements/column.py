from .winelement import WinElement
import pygame 
class Column(WinElement):
    def __init__(
            self,
            children,
            name="COLUMN",
            flex=1,
            padding=(0,0),
            gap=0,
            color=pygame.Color(0,0,0,0),
            position=(0,0),
            surface=None,
        ):
        WinElement.__init__(self, name, flex, color, position, surface)
        self.children = children
        self.padding = padding
        self.gap=gap

    def updatePose(self, parentPos, size, offset=(0,0), recalc=False):
        self.position = (parentPos[0]+offset[0], parentPos[1]+offset[1])
        self.offset = offset
        self.size = size

        if not recalc: return

        total = 0
        for c in self.children:
            total += c.flex

        _childcount = len(self.children)
        if _childcount == 1: self.gap=0
        _gpfact = (_childcount-1)*self.gap
        _tsize = (self.size[0]-self.padding[0]*2,
                  self.size[1]-self.padding[1]*2-_gpfact)
        _gpfact = 0 if _childcount<=1 else _gpfact/(_childcount-1)
        _gpfact /= 2

        _pos = (self.padding[0], self.padding[1])
        for c in self.children:
            _sz = (_tsize[0], c.flex/total*_tsize[1])
            c.updatePose(self.position, _sz, _pos, recalc)
            _pos = (_pos[0], _pos[1]+_sz[1]+self.gap)
    
    def render(self):
        if not self.surface:
            self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
            self.surface.convert_alpha()
        self.surface.fill(self.color)
        for c in self.children:
            c.draw(self.surface)

    def passEvents(self, events):
        self.handleEvents(events)
        for c in self.children:
            c.passEvents(events)

