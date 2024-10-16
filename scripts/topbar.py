from .winelements import *
from pygame import Color

class TopBar(Row):
    def __init__( self, name="TOPBAR", flex=1):
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
                            bold=True
                        ),
                    ], padding=(32, 12), flex=15),
                    WinElement(flex=4, color=Color(20, 30, 30)),
                ],
                name=name,
                flex=flex
            )
