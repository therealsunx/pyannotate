from .winelements import *
from .topbar import TopBar
from .debug import DebugInfo
from pygame import Color

class App(Window):
    def __init__(self):
        Window.__init__(self)

    def initializeChilds(self)->WinElement:
        self.canvas = Canvas(flex=8.0)
        self.debugger = DebugInfo(flex=0.3)
        self.sidebar = Column([
                self.debugger,
                Button(
                    child=Text(
                        text=" Button ",
                        flex=0.1, fontSize=20, bold=True,
                        color=Color(10,100,100)
                    ),
                    onClick= lambda o:print("Clicked ", o.name)
                )
            ], color=Color(10,10,10), flex=2)

        return Column([
                TopBar(),
                Row([self.canvas, self.sidebar],flex=15, gap=4)
            ],padding=(4,4),gap=4)

    def handleEvents(self, events):
        self.debugger.updateDebugInfo(self.canvas.cursor)

