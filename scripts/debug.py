from .winelements import *

class DebugInfo(Column):
    def __init__(self, flex=1.0):
        Column.__init__(
                self,
                children=self.initChilds(),
                flex=flex,
                padding=(8,4),
                color=Color(0,0,0,150)
            )

    def initChilds(self):
        self.cursorInfo = Text(value="x:0, y:0", fontSize=16)
        return [
                self.cursorInfo,
            ]

    def updateDebugInfo(self, cursor):
        self.cursorInfo.value = f"x:{cursor[0]}, y:{cursor[1]}"
