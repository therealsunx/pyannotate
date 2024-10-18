from .winelements import *
from pygame import Color

class TopBar(Row):
    def __init__( self, name="TOPBAR", flex=1, onExitClick = None):
        Row.__init__(
                self,
                children=[
                    Text("Q",
                         fontSize=32,
                         bold=True, italic=True,
                         flex=1,
                         color=Color(10,50,60),
                         padding=(16,8),
                    ),
                    Row([
                        Text(
                            "QuickCrop",
                            fontColor=Color(200,100,30),
                            bold=True,
                            fontSize=24
                        ),
                    ], padding=(32, 12), flex=15),
                    Button(child=Text("Exit", padding=(16,8), color=Color(100,0,0)), onClick=lambda _: self.exitClick())
                ],
                name=name,
                flex=flex
            )
        self.onExitClick = onExitClick
    def exitClick(self):
        if self.onExitClick: self.onExitClick()
