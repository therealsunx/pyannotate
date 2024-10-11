from pygame import Surface

class WinElement:
    def __init__(self, name="Window element", flex=1, surface=None):
        self.flex = flex
        self.name = name
        self.position = (0,0)
        if not surface:
            self.size = (0,0)
            self.surface = None
        else:
            self.surface = surface
            self.size = self.surface.get_size()

    def updatePose(self, position, size, recalc = False):
        self.position = position
        if not recalc: return
        self.size = size
        self.surface = Surface(self.size)
        self.render()
        print(f"{self.name} @ {self.position} of {self.size}")
        
    def render(self):
        if not self.surface: return
        self.surface.fill((120, 120, 0))

    def draw(self, window:Surface):
        if not self.surface: return
        window.blit(self.surface, self.position)

