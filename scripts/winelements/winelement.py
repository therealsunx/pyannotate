import pygame

class WinElement:
    def __init__(
            self,
            name="Window element",
            flex=1,
            color=pygame.Color(0,0,0,0),
            position=(0,0),
            surface=None,
        ):
        self.flex = flex
        self.name = name
        self.position = position
        self.offset = (0,0)
        self.color = color

        if not surface:
            self.size = (0,0)
            self.surface = None
        else:
            self.surface = surface
            self.size = self.surface.get_size()

    def updatePose(self, parentPos, size, offset=(0,0), recalc=False):
        self.position = (parentPos[0]+offset[0], parentPos[1]+offset[1])
        self.offset = offset
        self.size = size

    def render(self):
        if not self.surface: self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.surface.fill(self.color)

    def passEvents(self, events):
        self.handleEvents(events)

    def handleEvents(self, events):
        pass

    def setPosition(self, position):
        self.offset = (
                position[0]-self.position[0]+self.offset[0],
                position[1]-self.position[1]+self.offset[1],
            )
        self.position = position

    def setOffset(self, offset):
        self.position = (
                self.position[0]-self.offset[0]+offset[0],
                self.position[1]-self.offset[1]+offset[1],
            )
        self.offset = offset

    def draw(self, window:pygame.Surface):
        self.render()
        if not self.surface: return
        window.blit(self.surface, self.offset)

