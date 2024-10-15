import pygame as pg
from .winelement import WinElement

class Text(WinElement):
    fonts = {}

    @staticmethod
    def getFont(fontFamily, fontSize, bold=False, italic=False):
        fontKey = f"{fontFamily}{fontSize}{'B' if bold else ''}{'I' if italic else ''}"
        font = Text.fonts.get(fontKey)
        if font: return font
        font = pg.font.SysFont(fontFamily, fontSize, bold, italic)
        if not font: return pg.font.SysFont("Mono", fontSize, bold, italic)
        Text.fonts[fontKey] = font
        return font

    def __init__(
            self,
            text,
            fontFamily="Mono",
            fontSize=32,
            bold=False,
            italic=False,
            color=pg.Color(0,0,0,0),
            fontColor=pg.Color(255,255,255),
            name="TEXT",
            flex=1.0,
            position=(0,0),
            padding=(0,0),
            surface=None
        ):
        WinElement.__init__(self, name, flex, color, position, surface)
        self.text = text
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.bold = bold
        self.italic = italic
        self.padding = padding

    def render(self):
        font = Text.getFont(self.fontFamily, self.fontSize, self.bold, self.italic)
        text = font.render(self.text, True, self.fontColor)
        self.size = text.get_size()

        self.size = (self.size[0]+self.padding[0]*2, self.size[1]+self.padding[1]*2)
        self.surface = pg.Surface(self.size, pg.SRCALPHA)

        self.surface.fill(self.color)
        self.surface.blit(text, self.padding)

    def updatePose(self, parentPos, size, offset=(0,0), recalc=False):
        self.position = (parentPos[0]+offset[0], parentPos[1]+offset[1])
        self.offset = offset
        self.size = size
