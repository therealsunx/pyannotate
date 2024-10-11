from .winelement import WinElement
from pygame import Surface

class Row(WinElement):
    def __init__(self, children, padding=(0,0), gap=0):
        WinElement.__init__(self, "ROW")
        self.children = children
        self.padding = padding
        self.gap=gap

    def updatePose(self, position, size, recalc=False):
        self.position = position
        self.size = size
        if not recalc: return
        self.surface = Surface(self.size)
        self.surface.convert_alpha()

        total = 0
        for c in self.children:
            total += c.flex

        _childcount = len(self.children)
        if _childcount == 1: self.gap=0
        _gpfact = (_childcount-1)*self.gap
        _tsize = (self.size[0]-self.padding[0]-_gpfact,
                  self.size[1]-self.padding[1])
        _gpfact = 0 if _childcount<=1 else _gpfact/(_childcount-1)
        _gpfact /= 2

        _pos = (self.padding[0]//2, self.padding[1]//2)
        for c in self.children:
            _sz = (c.flex/total*_tsize[0], _tsize[1])
            c.updatePose(_pos, _sz, recalc)
            _pos = (_pos[0]+_sz[0]+self.gap, _pos[1])

        self.render()
    
    def render(self):
        if not self.surface: raise Exception("where is da fokin' surface ya cunt")
        #print(f"{self.name} @ {self.position} of {self.size}")
        self.surface.fill((20,200,20))
        for c in self.children:
            c.draw(self.surface)

