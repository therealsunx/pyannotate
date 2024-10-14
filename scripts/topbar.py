from .winelements import *
from pygame import Color

class TopBar(Row):
    def __init__( self, name="TOPBAR", flex=1):
        Row.__init__(
                self,
                children=[
                    Text(text="Q",
                         fontSize=48,
                         bold=True, italic=True,
                         flex=1,
                         color=Color(10,50,60),
                         padding=(16,8),
                    ),
                    Row([
                        Text(
                            text="QuickCrop",
                            fontColor=Color(200,100,30),
                            bold=True
                        ),
                    ], padding=(32, 20), flex=15),
                    WinElement(flex=4, color=Color(20, 30, 30)),
                ],
                name=name,
                flex=flex
            )
