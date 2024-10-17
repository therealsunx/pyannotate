from .column import Column
from pygame import Color

class List(Column):
    def __init__(
            self ,
            children,
            name="COLUMN",
            flex=1.0,
            padding=(0,0),
            id = 0,
            gap=0,
            color=Color(0,0,0,0),
            position=(0,0),
            ):
        Column.__init__(
            self ,
            children=children,
            name=name,
            flex=flex,
            padding=padding,
            gap=gap,
            color=color,
            position=position,
            id=id
        )

    def addChild(self, child):
        self.children.append(child)

    def popChild(self, index=-1):
        l = len(self.children)
        if l==0 or index>=l: return
        self.children.pop()

    def getChild(self, index=-1):
        l = len(self.children)
        if l==0 or index>=l: return None
        return self.children[index]

    def clear(self):
        self.children.clear()
    
    def removeChildByID(self, id):
        ind = -1
        for i,c in enumerate(self.children):
            if c.id == id:
                ind = i
                break
        if ind == -1: return
        self.children.pop(ind)

    def getChildCount(self):
        return len(self.children)
