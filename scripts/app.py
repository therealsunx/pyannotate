from .winelements import *
from .topbar import TopBar
from .canvas import Canvas
from pygame import Color

class App(Window):
    def __init__(self):
        Window.__init__(self)

    def initializeChilds(self)->WinElement:
        return Column([
            TopBar(),
            Row([
                Canvas(flex=8),
                WinElement(
                    flex=2,
                    color=Color(30,30,30)
                )
            ], flex=15)
            ], padding=(4,4), gap=4)
