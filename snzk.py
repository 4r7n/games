from tkinter import *
from tkinter import font as tkFont
import random

try:
    import snzkAI
except:
    pass

root=Tk()
root.geometry("525x525")
root.title("Aяυи")
root.resizable(False,False)
root.attributes('-topmost', 1)

AI = False
seq = ""
astep = 0
AIDepth = 0

class Cell:
    def __init__(self, x, y, bg="gray20", special=None):
        self.x = x
        self.y = y

        self.text = ""
        self.bg = bg
        self.fg = "yellow"
        self.special = None

        self.name = Button(root, text=self.text, bg=self.bg, fg=self.fg, command = None, borderwidth=0)

        self.name["font"] = tkFont.Font(family='Helvetica', size=int(50/2))

        self.name.place(x=self.x, y=self.y, height=35, width=35)

    def setc(self, nc):
        self.bg = nc
        self.name['bg'] = self.bg

    def setf(self, f):
        self.name['text'] = f

    def get(self):
        return [self.x, self.y, self.bg, self.name, self.special]

    def ss(self, spc):
        self.special = spc

        if spc==None:
            self.name.unbind("<Enter>")
            self.name.unbind("<Leave>")

        elif spc==1:
            self.name.bind("<Enter>", lambda event: enter1(int(self.x/35), int(self.y/35)))
            self.name.bind("<Leave>", lambda event: leave1(int(self.x/35), int(self.y/35)))

        elif spc==2:
            self.name.bind("<Enter>", on_enter)
            self.name.bind("<Leave>", on_leave)

    def setcm(self):
        self.name['command'] = strt

    def clrcm(self):
        self.name['command'] = None

def enter1(x, y):
    cells[x][y].setc("aquamarine")

    if not y==0:
        if cells[x][y-1].get()[4]==1:
            cells[x][y-1].setc("aquamarine3")

    if not y==14:
        if cells[x][y+1].get()[4]==1:
            cells[x][y+1].setc("aquamarine3")

    if not x==0:
        if cells[x-1][y].get()[4]==1:
            cells[x-1][y].setc("aquamarine3")

    if not x==14:
        if cells[x+1][y].get()[4]==1:
            cells[x+1][y].setc("aquamarine3")

    if not (x==14 or y==14):
        if cells[x+1][y+1].get()[4]==1:
            cells[x+1][y+1].setc("aquamarine4")

    if not (x==0 or y==14):
        if cells[x-1][y+1].get()[4]==1:
            cells[x-1][y+1].setc("aquamarine4")

    if not (x==14 or y==0):
        if cells[x+1][y-1].get()[4]==1:
            cells[x+1][y-1].setc("aquamarine4")

    if not (x==0 or y==0):
        if cells[x-1][y-1].get()[4]==1:
            cells[x-1][y-1].setc("aquamarine4")


    if not (y==0 or y==1):
        if cells[x][y-2].get()[4]==1:
            cells[x][y-2].setc("aquamarine4")

    if not (y==14 or y==13):
        if cells[x][y+2].get()[4]==1:
            cells[x][y+2].setc("aquamarine4")

    if not (x==0 or x==1):
        if cells[x-2][y].get()[4]==1:
            cells[x-2][y].setc("aquamarine4")

    if not (x==14 or x==13):
        if cells[x+2][y].get()[4]==1:
            cells[x+2][y].setc("aquamarine4")

def leave1(x, y):
    cells[x][y].setc("gray"+str(x+y))

    if not y==0:
        if cells[x][y-1].get()[4]==1:
            cells[x][y-1].setc("gray"+str(x+y-1))

    if not y==14:
        if cells[x][y+1].get()[4]==1:
            cells[x][y+1].setc("gray"+str(x+y+1))

    if not x==0:
        if cells[x-1][y].get()[4]==1:
            cells[x-1][y].setc("gray"+str(x+y-1))

    if not x==14:
        if cells[x+1][y].get()[4]==1:
            cells[x+1][y].setc("gray"+str(x+y+1))

    if not (x==14 or y==14):
        if cells[x+1][y+1].get()[4]==1:
            cells[x+1][y+1].setc("gray"+str(x+y+2))

    if not (x==0 or y==14):
        if cells[x-1][y+1].get()[4]==1:
            cells[x-1][y+1].setc("gray"+str(x+y))

    if not (x==14 or y==0):
        if cells[x+1][y-1].get()[4]==1:
            cells[x+1][y-1].setc("gray"+str(x+y))

    if not (x==0 or y==0):
        if cells[x-1][y-1].get()[4]==1:
            cells[x-1][y-1].setc("gray"+str(x+y-2))

    if not (y==0 or y==1):
        if cells[x][y-2].get()[4]==1:
            cells[x][y-2].setc("gray"+str(x+y-2))

    if not (y==14 or y==13):
        if cells[x][y+2].get()[4]==1:
            cells[x][y+2].setc("gray"+str(x+y+2))

    if not (x==0 or x==1):
        if cells[x-2][y].get()[4]==1:
            cells[x-2][y].setc("gray"+str(x+y-2))

    if not (x==14 or x==13):
        if cells[x+2][y].get()[4]==1:
            cells[x+2][y].setc("gray"+str(x+y+2))

def on_enter(event):
    cells[8][11].setc("darkorchid1")
    cells[6][11].setc("darkorchid1")
    cells[7][11].setc("darkorchid1")

def on_leave(event):
    cells[8][11].setc("darkorchid4")
    cells[6][11].setc("darkorchid4")
    cells[7][11].setc("darkorchid4")


cells = [[] for i in range(15)]

for x in range(15):
    for y in range(15):
        cells[x].append(Cell(x*35, y*35, bg="gray"+str(x+y)))

def display(digit,x,y):
    if digit==0:
        return [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]]
    elif digit==1:
        return [[x,y],[x+1,y],  [x+1,y+1],   [x+1,y+2],   [x+1,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]]
    elif digit==2:
        return [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]]
    elif digit==3:
        return [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x+2,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]]
    elif digit==4:
        return [[x,y],[x+2,y],  [x,y+1],[x+2,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x+2,y+3],    [x+2,y+4]]
    elif digit==5:
        return [[x,y],[x+1,y],[x+2,y],  [x,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x+2,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]]
    elif digit==6:
        return [[x,y],[x+1,y],[x+2,y],  [x,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]]
    elif digit==7:
        return [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],  [x+2,y+2],  [x+2,y+3],  [x+2,y+4]]
    elif digit==8:
        return [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]]
    elif digit==9:
        return [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x+2,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]]


def r2bmap(n):

    colours = []


    for i in range(n):

        red = int(255 - (255 * i / (n - 1)))
        blue = int(255 * i / (n - 1))
        colours.append((red, 0, blue))

    return ['#%02x%02x%02x'%item for item in colours]

def l_anim(score="025"):
    for i, row in enumerate(cells):

        for item in row:
            item.setc("yellow")
            item.setf("")

        if i==0:
            pass
        elif i==1:
            for item in cells[i-1]:
                item.setc("yellow2")

        elif i==2:
            for item in cells[i-1]:
                item.setc("yellow2")

            for item in cells[i-2]:
                item.setc("yellow3")

        else:
            for item in cells[i-1]:
                item.setc("yellow2")

            for item in cells[i-2]:
                item.setc("yellow3")

            for item in cells[i-3]:
                item.setc("yellow4")

        root.after(1)
        root.update()

        if not i in [0,1,2]:
            for j, item in enumerate(cells[i-3]):
                item.setc("gray"+str(i+j))

    for j, item in enumerate(cells[12]):
        item.setc("gray"+str(12+j))

    for item in cells[13]:
        item.setc("yellow4")

    for item in cells[14]:
        item.setc("yellow3")

    root.after(1)
    root.update()

    for j, item in enumerate(cells[13]):
        item.setc("gray"+str(13+j))

    for item in cells[14]:
        item.setc("yellow4")

    root.after(1)
    root.update()

    for j, item in enumerate(cells[14]):
        item.setc("gray"+str(14+j))

    root.after(1)
    root.update()

    for i in range(3):

        for item in display(int(score[0]), 2, 5):
            cells[item[0]][item[1]].setc("yellow")

        for item in display(int(score[1]), 6, 5):
            cells[item[0]][item[1]].setc("yellow")

        for item in display(int(score[2]), 10, 5):
            cells[item[0]][item[1]].setc("yellow")

        root.after(50)
        root.update()

        for item in display(int(score[0]), 2, 5):
            cells[item[0]][item[1]].setc("gray20")

        for item in display(int(score[1]), 6, 5):
            cells[item[0]][item[1]].setc("gray20")

        for item in display(int(score[2]), 10, 5):
            cells[item[0]][item[1]].setc("gray20")

        root.after(50)
        root.update()

    for item in display(int(score[0]), 2, 5):
        cells[item[0]][item[1]].setc("yellow")

    for item in display(int(score[1]), 6, 5):
        cells[item[0]][item[1]].setc("yellow")

    for item in display(int(score[2]), 10, 5):
        cells[item[0]][item[1]].setc("yellow")

    root.after(50)
    root.update()



class Object:
    def __init__(self, x, y, Type, name=None):
        self.x = x
        self.y = y

        self.Type = Type
        self.name = name

    def st(self, x, y):
        self.x = x
        self.y = y

    def s2(self, Type):
        self.Type = Type

    def gt(self):
        return [self.x, self.y, self.Type, self.name]

Map = [[] for i in range(15)]

for y in range(15):
    for x in range(15):
        Map[x].append(Object(x, y, "empty"))


def initi():
    global Map, dir, end, segm, head, vld, seq, astep

    seq, astep = "", 0

    Map = [[] for i in range(15)]

    for y in range(15):
        for x in range(15):
            Map[x].append(Object(x, y, "empty"))


    dir = "d"
    end = False

    segm = [Object(2, 6, "snake", name=1), Object(1, 6, "snake", name=2)]

    head = Object(3, 6, "head", name=0)

    Map[head.gt()[0]][head.gt()[1]] = head

    Map[11][6] = Object(11, 6, "food", name=0)
    #Map[9][8] = Object(9, 8, "food", name=0)
    #Map[13][8] = Object(13, 8, "food", name=0)
    #Map[9][4] = Object(9, 4, "food", name=0)
    #Map[13][4] = Object(13, 4, "food", name=0)


    for i in range(75):
        cdx, cdy = random.randint(0,14), random.randint(0,14)

        if Map[cdx][cdy].gt()[2]=="zzz":
            Map[cdx][cdy] = Object(cdx, cdy, "food", name=0)



    for item in segm:
        Map[item.gt()[0]][item.gt()[1]] = item

    vld = True


def setdir(event):
    global dir, vld

    if event.keysym in ["w", "a", "s", "d"] and vld==True:

        if not dir=="d" and event.keysym=="a":
            dir = event.keysym
        if not dir=="a" and event.keysym=="d":
            dir = event.keysym
        if not dir=="w" and event.keysym=="s":
            dir = event.keysym
        if not dir=="s" and event.keysym=="w":
            dir = event.keysym

        vld = False

def updt():
    global Map, segm
    size = len(segm)+1

    for i,item in enumerate(Map):
        for j,itm in enumerate(item):
            if itm.gt()[2]=="empty":
                cells[i][j].setc("gray"+str(i+j))

            elif itm.gt()[2]=="snake" or itm.gt()[2]=="head":
                cells[i][j].setc(r2bmap(size)[itm.gt()[3]])

            if itm.gt()[2]=="food":
                cells[i][j].setf("⬕")

            else:
                cells[i][j].setf("")


def move():
    global Map, dir, end, segm, head, vld

    if dir=="d":
        if head.gt()[0]==14:
            end = True

        elif Map[head.gt()[0]+1][head.gt()[1]].gt()[2]=="snake":
            end = True

        else:
            if Map[head.gt()[0]+1][head.gt()[1]].gt()[2]=="empty":
                Map[head.gt()[0]][head.gt()[1]] = Object(head.gt()[0], head.gt()[1], "empty")

                hcd = head.gt()[:2]

                head.st(head.gt()[0] + 1, head.gt()[1])
                Map[head.gt()[0]][head.gt()[1]] = head

                Map[segm[-1].gt()[0]][segm[-1].gt()[1]] = Object(segm[-1].gt()[0], segm[-1].gt()[1], "empty")

                for i in range(len(segm)-1, 0, -1):
                    segm[i].st(segm[i-1].gt()[0], segm[i-1].gt()[1])

                segm[0].st(hcd[0], hcd[1])

                for item in segm:
                    Map[item.gt()[0]][item.gt()[1]] = item


            elif Map[head.gt()[0]+1][head.gt()[1]].gt()[2]=="food":
                Map[head.gt()[0]][head.gt()[1]] = Object(head.gt()[0], head.gt()[1], "empty")

                hcd = head.gt()[:2]

                head.st(head.gt()[0] + 1, head.gt()[1])
                Map[head.gt()[0]][head.gt()[1]] = head

                Map[segm[-1].gt()[0]][segm[-1].gt()[1]] = Object(segm[-1].gt()[0], segm[-1].gt()[1], "empty")

                ncd = segm[-1].gt()[:2]

                for i in range(len(segm)-1, 0, -1):
                    segm[i].st(segm[i-1].gt()[0], segm[i-1].gt()[1])

                segm[0].st(hcd[0], hcd[1])

                segm.append(Object(ncd[0], ncd[1], "snake", name=(segm[-1].gt()[3]+1)))

                for item in segm:
                    Map[item.gt()[0]][item.gt()[1]] = item

                empty = []
                for item in Map:
                    for cell in item:
                        if cell.gt()[2]=="empty":
                            empty.append(cell)

                if not empty==[]:
                    ch = random.choice(empty)
                    Map[ch.gt()[0]][ch.gt()[1]] = Object(ch.gt()[0], ch.gt()[1], "food")


    if dir=="a":
        if head.gt()[0]==0:
            end = True

        elif Map[head.gt()[0]-1][head.gt()[1]].gt()[2]=="snake":
            end = True

        else:
            if Map[head.gt()[0]-1][head.gt()[1]].gt()[2]=="empty":
                Map[head.gt()[0]][head.gt()[1]] = Object(head.gt()[0], head.gt()[1], "empty")

                hcd = head.gt()[:2]

                head.st(head.gt()[0] - 1, head.gt()[1])
                Map[head.gt()[0]][head.gt()[1]] = head

                Map[segm[-1].gt()[0]][segm[-1].gt()[1]] = Object(segm[-1].gt()[0], segm[-1].gt()[1], "empty")

                for i in range(len(segm)-1, 0, -1):
                    segm[i].st(segm[i-1].gt()[0], segm[i-1].gt()[1])

                segm[0].st(hcd[0], hcd[1])

                for item in segm:
                    Map[item.gt()[0]][item.gt()[1]] = item


            elif Map[head.gt()[0]-1][head.gt()[1]].gt()[2]=="food":
                Map[head.gt()[0]][head.gt()[1]] = Object(head.gt()[0], head.gt()[1], "empty")

                hcd = head.gt()[:2]

                head.st(head.gt()[0] - 1, head.gt()[1])
                Map[head.gt()[0]][head.gt()[1]] = head

                Map[segm[-1].gt()[0]][segm[-1].gt()[1]] = Object(segm[-1].gt()[0], segm[-1].gt()[1], "empty")

                ncd = segm[-1].gt()[:2]

                for i in range(len(segm)-1, 0, -1):
                    segm[i].st(segm[i-1].gt()[0], segm[i-1].gt()[1])

                segm[0].st(hcd[0], hcd[1])

                segm.append(Object(ncd[0], ncd[1], "snake", name=(segm[-1].gt()[3]+1)))

                for item in segm:
                    Map[item.gt()[0]][item.gt()[1]] = item

                empty = []
                for item in Map:
                    for cell in item:
                        if cell.gt()[2]=="empty":
                            empty.append(cell)

                if not empty==[]:
                    ch = random.choice(empty)
                    Map[ch.gt()[0]][ch.gt()[1]] = Object(ch.gt()[0], ch.gt()[1], "food")


    if dir=="w":
        if head.gt()[1]==0:
            end = True

        elif Map[head.gt()[0]][head.gt()[1]-1].gt()[2]=="snake":
            end = True

        else:
            if Map[head.gt()[0]][head.gt()[1]-1].gt()[2]=="empty":
                Map[head.gt()[0]][head.gt()[1]] = Object(head.gt()[0], head.gt()[1], "empty")

                hcd = head.gt()[:2]

                head.st(head.gt()[0], head.gt()[1] - 1)
                Map[head.gt()[0]][head.gt()[1]] = head

                Map[segm[-1].gt()[0]][segm[-1].gt()[1]] = Object(segm[-1].gt()[0], segm[-1].gt()[1], "empty")

                for i in range(len(segm)-1, 0, -1):
                    segm[i].st(segm[i-1].gt()[0], segm[i-1].gt()[1])

                segm[0].st(hcd[0], hcd[1])

                for item in segm:
                    Map[item.gt()[0]][item.gt()[1]] = item


            elif Map[head.gt()[0]][head.gt()[1]-1].gt()[2]=="food":
                Map[head.gt()[0]][head.gt()[1]] = Object(head.gt()[0], head.gt()[1], "empty")

                hcd = head.gt()[:2]

                head.st(head.gt()[0], head.gt()[1] - 1)
                Map[head.gt()[0]][head.gt()[1]] = head

                Map[segm[-1].gt()[0]][segm[-1].gt()[1]] = Object(segm[-1].gt()[0], segm[-1].gt()[1], "empty")

                ncd = segm[-1].gt()[:2]

                for i in range(len(segm)-1, 0, -1):
                    segm[i].st(segm[i-1].gt()[0], segm[i-1].gt()[1])

                segm[0].st(hcd[0], hcd[1])

                segm.append(Object(ncd[0], ncd[1], "snake", name=(segm[-1].gt()[3]+1)))

                for item in segm:
                    Map[item.gt()[0]][item.gt()[1]] = item

                empty = []
                for item in Map:
                    for cell in item:
                        if cell.gt()[2]=="empty":
                            empty.append(cell)

                if not empty==[]:
                    ch = random.choice(empty)
                    Map[ch.gt()[0]][ch.gt()[1]] = Object(ch.gt()[0], ch.gt()[1], "food")

    if dir=="s":
        if head.gt()[1]==14:
            end = True

        elif Map[head.gt()[0]][head.gt()[1]+1].gt()[2]=="snake":
            end = True

        else:
            if Map[head.gt()[0]][head.gt()[1]+1].gt()[2]=="empty":
                Map[head.gt()[0]][head.gt()[1]] = Object(head.gt()[0], head.gt()[1], "empty")

                hcd = head.gt()[:2]

                head.st(head.gt()[0], head.gt()[1] + 1)
                Map[head.gt()[0]][head.gt()[1]] = head

                Map[segm[-1].gt()[0]][segm[-1].gt()[1]] = Object(segm[-1].gt()[0], segm[-1].gt()[1], "empty")

                for i in range(len(segm)-1, 0, -1):
                    segm[i].st(segm[i-1].gt()[0], segm[i-1].gt()[1])

                segm[0].st(hcd[0], hcd[1])

                for item in segm:
                    Map[item.gt()[0]][item.gt()[1]] = item


            elif Map[head.gt()[0]][head.gt()[1]+1].gt()[2]=="food":
                Map[head.gt()[0]][head.gt()[1]] = Object(head.gt()[0], head.gt()[1], "empty")

                hcd = head.gt()[:2]

                head.st(head.gt()[0], head.gt()[1] + 1)
                Map[head.gt()[0]][head.gt()[1]] = head

                Map[segm[-1].gt()[0]][segm[-1].gt()[1]] = Object(segm[-1].gt()[0], segm[-1].gt()[1], "empty")

                ncd = segm[-1].gt()[:2]

                for i in range(len(segm)-1, 0, -1):
                    segm[i].st(segm[i-1].gt()[0], segm[i-1].gt()[1])

                segm[0].st(hcd[0], hcd[1])

                segm.append(Object(ncd[0], ncd[1], "snake", name=(segm[-1].gt()[3]+1)))

                for item in segm:
                    Map[item.gt()[0]][item.gt()[1]] = item

                empty = []
                for item in Map:
                    for cell in item:
                        if cell.gt()[2]=="empty":
                            empty.append(cell)

                if not empty==[]:
                    ch = random.choice(empty)
                    Map[ch.gt()[0]][ch.gt()[1]] = Object(ch.gt()[0], ch.gt()[1], "food")

    vld = True

def play():
    global end, segm, AI, seq, Map, dir, astep, AIDepth
    updt()

    if AI==False:
        root.bind("<KeyRelease>", setdir)

    else:
        if random.randint(1,15)==99:
            seq = ""

        if seq=="":
            dat = snzkAI.djalg([[item.gt() for item in it] for it in Map], dir, [it.gt() for it in segm], depth=AIDepth)

            seq = dat[1]

            if not str(dat[0])[0]=="e":
                astep+=1

            print(str(astep)+":"+str(dat))

        dir = seq[0]
        seq = seq[1:]

    move()
    updt()
    if end==False:
        if AI==False:
            root.after(100, play)

        else:
            root.after(10, play)

    else:
        score = len(segm) - 2

        if len(str(score))==1:
            score = "00"+str(score)

        elif len(str(score))==2:
            score = "0"+str(score)

        else:
            score = str(score)

        l_anim(score=score)


        for item in cells:
            for itm in item:
                if not itm.get()[2]=="yellow":
                    itm.setc("gray"+str(sum([int(i/35) for i in itm.get()[:2]])))
                    itm.ss(1)

        cells[8][11].setc("darkorchid4")
        cells[6][11].setc("darkorchid4")
        cells[7][11].setc("darkorchid4")
        cells[8][11].ss(2)
        cells[6][11].ss(2)
        cells[7][11].ss(2)

        cells[8][11].setcm()
        cells[6][11].setcm()
        cells[7][11].setcm()


def strt():
    for item in cells:
        for itm in item:
            itm.clrcm()
            itm.ss(None)
            itm.setc("gray"+str(sum([int(i/35) for i in itm.get()[:2]])))

    initi()
    play()

typeA = lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x+2,y+3],[x,y+3],  [x,y+4], [x+2,y+4]]
typeR = lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x,y+1],  [x,y+2],  [x,y+3],  [x,y+4]]
typeU = lambda x, y: [[x,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]]
typeN = lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+2,y+4]]

for item in typeA(0,0):
    cells[item[0]][item[1]].setc("yellow")

for item in typeR(4,0):
    cells[item[0]][item[1]].setc("yellow")

for item in typeU(8,0):
    cells[item[0]][item[1]].setc("yellow")

for item in typeN(12, 0):
    cells[item[0]][item[1]].setc("yellow")

for item in cells:
    for itm in item:
        if not itm.get()[2]=="yellow":
            itm.ss(1)

cells[8][11].setc("darkorchid4")
cells[6][11].setc("darkorchid4")
cells[7][11].setc("darkorchid4")
cells[8][11].ss(2)
cells[6][11].ss(2)
cells[7][11].ss(2)

cells[8][11].setcm()
cells[6][11].setcm()
cells[7][11].setcm()


root.mainloop()