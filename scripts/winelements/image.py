from .winelement import WinElement
import pygame as pg

class Image(WinElement):
    def __init__(
            self,
            src,
            name="Image",
            flex=1.0,
            color=pg.Color(0,0,0,0),
            position=(0,0),
            surface=None
        ):
        WinElement.__init__(self, name, flex, color, position, surface)
        self.src = src
        self.scale = 1

    def render(self):
        if not self.surface:
            self.surface = pg.Surface(self.size, pg.SRCALPHA)
            self.surface.convert_alpha()
        self.img = pg.image.load(self.src).convert_alpha()
        org_size = self.img.get_size()

        if org_size[0]>org_size[1]:
            self.scale = self.size[0]/org_size[0]
        else:
            self.scale = self.size[1]/org_size[1]
        
        self.img = pg.transform.smoothscale_by(self.img, self.scale)
        self.surface.blit(self.img, (0,0))
