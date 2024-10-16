# canvas on steroids

from .winelements import Canvas, Color, Gizmo

class StrdCanvas(Canvas):
    def __init__(
            self,
            defchilds = [],
            background=None,
            position=(0,0),
            color=Color(20,20,20),
            flex=1.0,
            onSelect = None
        ):
        Canvas.__init__(
                self,
                background=background,
                position=position,
                color=color,
                flex=flex,
                onSelect=onSelect
            )
        self.gizmochilds = defchilds

    def render(self):
        Canvas.render(self)
        for c in self.gizmochilds:
            c.draw(self.surface)

    def addGizmoChild(self, child):
        self.gizmochilds.append(child)

    def popGizmoChild(self, index=-1):
        l = len(self.gizmochilds)
        if l == 0 or l <= index: return
        self.gizmochilds.pop(index)
            
