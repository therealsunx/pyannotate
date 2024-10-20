from .winelements import *
from .topbar import TopBar
from .debug import DebugInfo
from .strdcanvas import StrdCanvas

import glob, sys
from pygame import KEYDOWN
from pygame import image as pyimage
from pathlib import Path

class App(Window):
    def __init__(self):
        dir = sys.argv[1] if len(sys.argv)>1 else "./"
        if dir[-1] != '/': dir = dir+"/"
        fmts = ["png", "jpg", "jpeg"]
        self.imgs = []
        for fmt in fmts:
            self.imgs = self.imgs+glob.glob(f"{dir}*.{fmt}")
        self.curInd = 0
        self.charIDs = {}

        Window.__init__(self)

    def initializeChilds(self)->WinElement:
        self.canvas = StrdCanvas(
                flex=7,
                background=self.currentImage(),
                onSelect=self.onSelectCanvas
            )
        self.debugger = DebugInfo(flex=2)

        self.rectList = List([], flex=8, padding=(4,4), gap=2)

        self.curDirText = Text("proc_imgs", padding=(4,4), color=Color(10,10,10), flex=2)
        self.namePrefText = Text("img", padding=(4,4), color=Color(10,10,10), flex=2)
 
        f_info = Column([
            Row([
                Text("Set NamePrefix", padding=(0,6)),
                Input(
                    padding=(8,4), flex=4,
                    color=Color(10,10,10,200),
                    onSubmit=self.setNamePrefix
                ),
            ], padding=(4,4), gap=4),
            Row([
                Text("NamePrefix", padding=(4,4)),
                self.namePrefText
            ]),
            Row([
                Text("Set Dir", padding=(0,6)),
                Input(
                    padding=(8,4), flex=4,
                    color=Color(10,10,10,200),
                    onSubmit=self.setCurDir
                ),
            ], padding=(4,4), gap=4),
            Row([
                Text("Current Dir", padding=(4,4)),
                self.curDirText
            ])
        ], flex=3, gap=4)
        hairline = WinElement(flex=0.04, color=Color(255,255,255))
        submitbtn = Button(Text(
                            "Submit",
                            bold=True,
                            color=Color(0,200,50,200),
                            padding=(16,4)
                            ), onClick=lambda _:self.onSubmit())
        skipbtn = Button(Text(
                            "Skip",
                            bold=True,
                            color=Color(200,0,50,200),
                            padding=(16,4)
                            ), onClick=lambda _:self.nextImg())
        prevbtn = Button(Text(
                            "Previous",
                            bold=True,
                            color=Color(200,200,0,200),
                            padding=(16,4)
                            ), onClick=lambda _:self.nextImg(-1))

        self.sidebar = Column([
                self.debugger,
                hairline,
                Column([
                    f_info,
                    self.rectList
                ], flex=17, padding=(4,4), color=Color(20,30,60)),
                hairline,
                Row([
                    submitbtn,
                    prevbtn,
                    skipbtn
                ],
                gap=16, padding=(4,4), flex=1)
            ], color=Color(10,10,10), flex=3)

        return Column([
            TopBar(onExitClick = self.exitClick),
                Row([self.canvas, self.sidebar],flex=15, gap=4)
            ],padding=(4,4),gap=4)

    def exitClick(self):
        self.shouldExit = True

    def handleLateEvents(self, events):
        self.debugger.updateDebugInfo(
                self.canvas.cursor,
                self.canvas.getSelection()
            )
        
        for e in events:
            if e.type == KEYDOWN and e.unicode == '\b':
                self.canvas.popGizmoChild()
                self.rectList.popChild()

    def onSelectCanvas(self, rect):
        if rect[2]<10 or rect[2]<10: return
        ngz = Gizmo(position=rect[:2], size=rect[2:], borderColor=Color(255,255,0))
        self.canvas.addGizmoChild(ngz)
        self.rectList.addChild(Text(f"{rect}", color=Color(30,30,30), flex=0.03))

    def nextImg(self, dir=1):
        nc = self.curInd+dir
        if nc < 0: return
        if nc > len(self.imgs): nc = 0
        self.curInd = nc
        self.canvas.background.setImage(self.currentImage())
        self.canvas.clearGizmos()
        self.rectList.clear()

    def currentImage(self):
        if self.curInd >= len(self.imgs): return None
        return self.imgs[self.curInd]
    
    def setCurDir(self, dir):
        self.curDirText.value = dir

    def setNamePrefix(self, prefix):
        self.namePrefText.value = prefix
    
    def onSubmit(self): 
        for i,gizmo in enumerate(self.canvas.gizmochilds):
            self.saveRect(gizmo, name=f"{self.namePrefText.value}{i}")
        self.canvas.clearGizmos()
        self.rectList.clear()
    
    def saveRect(self, gizmo, name="img01"):
        sf = self.canvas.getChunkFromGizmo(gizmo)
        if not sf: return

        if self.charIDs.get(name):
            self.charIDs[name]+=1;
        else:
            self.charIDs[name] = 1;
        curID = self.charIDs[name]
        cdir = f"{self.curDirText.value}/{name}"
        Path(cdir).mkdir(parents=True, exist_ok=True)
        pyimage.save(sf, f"{cdir}/{curID}.png")

