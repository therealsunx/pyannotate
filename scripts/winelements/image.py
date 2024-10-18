from .winelement import WinElement
import pygame as pg

class Image(WinElement):
    def __init__(
            self,
            src,
            name="Image",
            id = 0,
            flex=1.0,
            color=pg.Color(0,0,0),
            position=(0,0),
            surface=None
        ):
        WinElement.__init__(self, name, flex, color, position, id, surface)
        self.src = src
        self.scale = 1

    def setImage(self, src):
        self.src = src
        if self.src: self._renderImg(self.src)
        else: self.surface.fill(self.color)

    def _renderImg(self, src):
        self.org_image = pg.image.load(src).convert_alpha()
        org_size = self.org_image.get_size()

        if org_size[0]>org_size[1]:
            self.scale = self.size[0]/org_size[0]
        else:
            self.scale = self.size[1]/org_size[1]
        
        self.img = pg.transform.smoothscale_by(self.org_image, self.scale)
        self.surface.blit(self.img, (0,0))

    def render(self):
        if self.surface: return

        self.surface = pg.Surface(self.size, pg.SRCALPHA)
        self.surface.convert_alpha()
        self.setImage(self.src)

