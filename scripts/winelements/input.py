from .text import Text
from pygame import mouse, Color, Surface
from pygame import MOUSEBUTTONDOWN, SRCALPHA, KEYDOWN, K_BACKSPACE
from pygame import draw

class Input(Text):
    def __init__(
            self,
            value = "",
            fontFamily="Mono",
            fontSize=16,
            bold=False,
            italic=False,
            color=Color(0,0,0,0),
            fontColor=Color(255,255,255),
            name="INPUT",
            id = 0,
            flex=1.0,
            position=(0,0),
            padding=(0,0),
            onSubmit=None
        ):
        Text.__init__(
                self,
                value=value ,
                fontFamily=fontFamily,
                fontSize=fontSize,
                bold=bold,
                italic=italic,
                color=color,
                fontColor=fontColor,
                name=name,
                flex=flex,
                position=position,
                id=id,
                padding=padding,
                surface=None
            )
        self.focused = False
        self.onSubmit = onSubmit

    def handleEvents(self, events):
        ms = mouse.get_pos()
        rect = (*self.position,
                self.position[0]+self.size[0],
                self.position[1]+self.size[1])
        
        hitt = rect[0]<=ms[0]<=rect[2] and rect[1]<=ms[1]<=rect[3]
        if not (self.focused or hitt): return
        for e in events:
            if e.type == MOUSEBUTTONDOWN:
                self.focused = hitt
                break
            if not self.focused: continue
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:
                    self.value = self.value[:-1]
                elif e.unicode == '\x1b':
                    self.focused = False
                elif e.unicode == '\r':
                    if self.onSubmit: self.onSubmit(self.value)
                    self.focused = False
                else:
                    self.value += e.unicode
            
    def render(self):
        font = Text.getFont(self.fontFamily, self.fontSize, self.bold, self.italic)
        value = font.render(self.value + ('|' if self.focused else ''), True, self.fontColor)

        self.size = (self.size[0], value.get_height()+self.padding[1]*2)
        self.surface = Surface(self.size, SRCALPHA)

        self.surface.fill(self.color)
        draw.rect(self.surface,
                  Color(255,255,255) if self.focused else Color(100,100,100),
                  (0,0,*self.size), width=1, border_radius=6)
        self.surface.blit(value, self.padding)

