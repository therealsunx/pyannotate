from .winelements import *
from .topbar import TopBar
from .debug import DebugInfo
from .strdcanvas import StrdCanvas

import glob
from pygame import KEYDOWN

class App(Window):
    def __init__(self):
        Window.__init__(self)
        imgs = glob.glob("rawimg/*.jpg")
        print(imgs)

    def initializeChilds(self)->WinElement:
        self.canvas = StrdCanvas(
                flex=8.0,
                background="rawimg/test.jpg",
                onSelect=self.onSelectCanvas
            )
        self.debugger = DebugInfo(flex=2)
        self.sidebar = Column([
                self.debugger,
                WinElement(flex=0.04, color=Color(255,255,255)),
                Column([
                    Column([
                        Text("Add Dir"),
                        Input(
                            padding=(8,4),
                            color=Color(10,10,10,200),
                            onSubmit=lambda val:print(val)
                        ),
                    ], flex=1, padding=(4,4)),

                    Column([
                        Text("Dir name", flex=.05, padding=(8,4), color=Color(10,10,10)),
                        Text("Dir name", flex=.05, padding=(8,4), color=Color(10,10,10)),
                        Text("Dir name", flex=.05, padding=(8,4), color=Color(10,10,10)),
                        Text("Dir name", flex=.05, padding=(8,4), color=Color(10,10,10)),
                    ], flex=9, padding=(4,4)),
                ], flex=17, padding=(4,4), color=Color(20,30,60)),

                WinElement(flex=0.04, color=Color(255,255,255)),

                Row([
                    Button(
                        child=Text(
                            "Submit",
                            bold=True,
                            color=Color(0,200,50,200),
                            padding=(16,4)
                        ),
                        onClick=None
                    ),
                    Button(
                        child=Text(
                            "Skip",
                            bold=True,
                            color=Color(200,0,50,200),
                            padding=(16,4)
                        ),
                        onClick=None
                    ),
                ],
                gap=16, padding=(4,4), flex=1)
            ], color=Color(10,10,10), flex=2)

        return Column([
                TopBar(),
                Row([self.canvas, self.sidebar],flex=15, gap=4)
            ],padding=(4,4),gap=4)

    def handleLateEvents(self, events):
        self.debugger.updateDebugInfo(
                self.canvas.cursor,
                self.canvas.getSelection()
            )
        
        for e in events:
            if e.type == KEYDOWN and e.unicode == '\b':
                self.canvas.popGizmoChild()

    def onSelectCanvas(self, rect):
        if rect[2]<10 or rect[2]<10: return
        ngz = Gizmo(
                position=(rect[0], rect[1]),
                size=(rect[2], rect[3]),
                borderColor=Color(255,255,0)
            )
        self.canvas.addGizmoChild(ngz)
