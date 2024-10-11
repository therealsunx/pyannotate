from .winelements import *
import pygame as pg
pg.init()

WIN_SIZE = (1280, 760)
WIN_NAME = "QuickCrop"

class Window(WinElement):
    def __init__(self):
        WinElement.__init__(
                self,
                name=WIN_NAME,
                flex=1,
                surface=pg.display.set_mode(WIN_SIZE)
            )
        pg.display.set_caption(self.name)
        self.clock = pg.time.Clock()
        self.shouldExit = False

        self.initializeChilds()

    def initializeChilds(self):
        self.child = Column([
            Row([
                WinElement(),
                WinElement()
            ], gap=16),
            WinElement(),
            WinElement()
            ], padding=(32, 32), gap=16)
        self.child.updatePose(self.position, self.size, True)

    def render(self):
        if not self.surface: return
        self.surface.fill((0,100,100))
        self.child.render()
        self.child.draw(self.surface)

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.shouldExit = True

    def update(self):
        self.clock.tick(60)
        pg.display.update()

    def run(self):
        while not self.shouldExit:
            self.handleEvents()
            self.render()
            self.update()
        pg.quit()
        exit(0)

