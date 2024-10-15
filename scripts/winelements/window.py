from . import *
from typing import List
import pygame as pg
pg.init()

WIN_SIZE = (1440, 800)
WIN_NAME = "QuickCrop"

class Window(WinElement):
    def __init__(self):
        WinElement.__init__(
                self,
                name=WIN_NAME,
                flex=1,
                position=(0,0),
                surface=pg.display.set_mode(WIN_SIZE)
            )
        pg.display.set_caption(self.name)
        self.clock = pg.time.Clock()
        self.shouldExit = False
        self.child = self.initializeChilds()
    
    def initializeChilds(self)->WinElement:
        titlesz = 64
        pos = (
                32,
                (self.size[1]-titlesz)//2
            )
        return Text(text="Py-UI", fontSize=64, position=pos)

    def render(self):
        if not self.surface: return
        self.surface.fill(pg.Color(0,0,0))
        self.child.draw(self.surface)

    def passEvents(self, events:List[pg.event.Event]):
        self._processMasterEvents(events)
        self.handleEvents(events)
        self.child.passEvents(events)

    def handleEvents(self, events:List[pg.event.Event]):
        pass

    def _processMasterEvents(self, events:List[pg.event.Event]):
        for event in events:
            if event.type == pg.QUIT:
                self.shouldExit = True
                break

    def update(self):
        self.clock.tick(60)
        pg.display.update()

    def updatePose(self, parentPos, size, offset=(0,0), recalc=False):
        self.position = (parentPos[0]+offset[0], parentPos[1]+offset[1])
        self.offset = offset
        self.size = size
        self.child.updatePose(self.position, self.size, recalc=recalc)

    def run(self):
        while not self.shouldExit:
            self.passEvents(pg.event.get())
            self.updatePose(self.position, self.size, recalc=True)
            self.render()
            self.update()
        pg.quit()
        exit(0)

