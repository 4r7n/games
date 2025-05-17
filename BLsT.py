from tkinter import *
from tkinter import font as tkFont
import random

try:
    import blstai
except:
    pass

AI = False


#       /\    __         __
#      /__\  |    |  |  |  |
#     /    \ |    |__|  |  |


root=Tk()
root.geometry("460x720")
root.title("Aяυи")
root.resizable(False,False)
root.attributes('-topmost', 1)

Button(root, bg="gray40", state="disabled", borderwidth = 6).place(x = 0, y = 0, height = 720, width = 460)
Button(root, bg="black", state="disabled", borderwidth = 0).place(x = 6, y = 6, height = 80, width = 446)

Alpha = {
    "0" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "1" : lambda x, y: [[x,y],[x+1,y],  [x+1,y+1],   [x+1,y+2],   [x+1,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "2" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "3" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x+2,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "4" : lambda x, y: [[x,y],[x+2,y],  [x,y+1],[x+2,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x+2,y+3],    [x+2,y+4]],
    "5" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x+2,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "6" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "7" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],  [x+2,y+2],  [x+2,y+3],  [x+2,y+4]],
    "8" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "9" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x+2,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "A" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x+2,y+3],[x,y+3],  [x,y+4], [x+2,y+4]],
    "B" : lambda x, y: [[x,y],[x+1,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4]],
    "C" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x,y+1], [x,y+2], [x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "D" : lambda x, y: [[x,y],[x+1,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4]],
    "E" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "F" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x,y+3],  [x,y+4]],
    "G" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x,y+1],  [x+2,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "H" : lambda x, y: [[x,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+2,y+4]],
    "I" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+1,y+1],   [x+1,y+2],   [x+1,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "J" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+1,y+1],   [x+1,y+2],   [x+1,y+3],  [x,y+4],[x+1,y+4]],
    "K" : lambda x, y: [[x,y],[x+2,y],  [x+1,y+1],[x,y+1],  [x,y+2],  [x+1,y+3],[x,y+3],  [x,y+4],[x+2,y+4]],
    "L" : lambda x, y: [[x,y],  [x,y+1],  [x,y+2],  [x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "M" : None,
    "N" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+2,y+4]],
    "O" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "P" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],[x+1,y+2],  [x,y+3],  [x,y+4]],
    "Q" : None,
    "R" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x,y+1],  [x,y+2],  [x,y+3],  [x,y+4]],
    "S" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x,y+1],  [x+2,y+2],[x+1,y+2],[x,y+2],  [x+2,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "T" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+1,y+1],   [x+1,y+2],   [x+1,y+3],  [x+1,y+4]],
    "U" : lambda x, y: [[x,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    "V" : lambda x, y: [[x,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+2,y+2],[x,y+2],  [x+2,y+3],[x,y+3],  [x+1,y+4]],
    "W" : None,
    "X" : lambda x, y: [[x,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+1,y+2],  [x,y+3],[x+2,y+3],  [x+2,y+4],[x,y+4]],
    "Y" : lambda x, y: [[x,y],[x+2,y],  [x+2,y+1],[x,y+1],  [x+1,y+2],  [x+1,y+3],  [x+1,y+4]],
    "Z" : lambda x, y: [[x,y],[x+1,y],[x+2,y],  [x+2,y+1],  [x+1,y+2],  [x,y+3],  [x,y+4],[x+1,y+4],[x+2,y+4]],
    ":" : lambda x, y: [[x,y+1],  [x,y+3]],
    "+" : lambda x, y: [[x+1,y+1], [x+2,y+2],[x,y+2],[x+1,y+2], [x+1,y+3]]
}


blckt = [
    lambda x, y: [[x,y],[x+1,y]],
    lambda x, y: [[x,y],[x+1,y],[x-1,y]],
    lambda x, y: [[x,y],[x+1,y],[x+2,y],[x-1,y]],
    lambda x, y: [[x,y],[x+1,y],[x+2,y],[x-2,y],[x-1,y]],   ####

    lambda x, y: [[x,y],[x,y+1]],                           #
    lambda x, y: [[x,y],[x,y+1],[x,y-1]],                   #
    lambda x, y: [[x,y],[x,y+1],[x,y+2],[x,y-1]],           #
    lambda x, y: [[x,y],[x,y+1],[x,y+2],[x,y-1],[x,y-2]],   #

    lambda x, y: [[x,y],[x,y+1],[x+1,y],[x+1,y+1]],                                                   ##
    lambda x, y: [[x,y],[x,y+1],[x+1,y],[x+1,y+1],[x,y-1],[x-1,y],[x-1,y-1],[x+1,y-1],[x-1,y+1]],     ##
    lambda x, y: [[x,y],[x,y+1],[x+1,y],[x+1,y+1],[x-1,y],[x-1,y+1]],
    lambda x, y: [[x,y],[x,y+1],[x+1,y],[x+1,y+1],[x,y-1],[x+1,y-1]],

    lambda x, y: [[x,y],[x+1,y],[x-1,y],[x,y+1]],           #
    lambda x, y: [[x,y],[x+1,y],[x-1,y],[x,y-1]],          ###
    lambda x, y: [[x,y],[x,y+1],[x,y-1],[x+1,y]],
    lambda x, y: [[x,y],[x,y+1],[x,y-1],[x-1,y]],

    lambda x, y: [[x,y],[x+1,y],[x-1,y],[x-1,y+1]],
    lambda x, y: [[x,y],[x+1,y],[x-1,y],[x+1,y+1]],          #
    lambda x, y: [[x,y],[x+1,y],[x-1,y],[x,y-1]],            ###
    lambda x, y: [[x,y],[x+1,y],[x-1,y],[x+1,y-1]],

    lambda x, y: [[x,y],[x,y+1],[x,y-1],[x+1,y+1]],
    lambda x, y: [[x,y],[x,y+1],[x,y-1],[x+1,y-1]],          #
    lambda x, y: [[x,y],[x,y+1],[x,y-1],[x-1,y+1]],          #
    lambda x, y: [[x,y],[x,y+1],[x,y-1],[x-1,y-1]],          ##

    lambda x, y: [[x,y],[x,y+1],[x+1,y]],
    lambda x, y: [[x,y],[x,y+1],[x-1,y]],                  #
    lambda x, y: [[x,y],[x,y-1],[x+1,y]],                 ##
    lambda x, y: [[x,y],[x,y+1],[x-1,y]],

    lambda x, y: [[x,y],[x-1,y],[x+1,y+1],[x,y+1]],
    lambda x, y: [[x,y],[x-1,y],[x+1,y-1],[x,y-1]],         ##
    lambda x, y: [[x,y],[x,y-1],[x+1,y+1],[x+1,y]],        ##
    lambda x, y: [[x,y],[x,y-1],[x-1,y+1],[x-1,y]],

    lambda x, y: [[x,y],[x+1,y],[x+2,y],[x,y+1],[x,y+2]],
    lambda x, y: [[x,y],[x+1,y],[x+2,y],[x,y-1],[x,y-2]],   ###
    lambda x, y: [[x,y],[x-1,y],[x-2,y],[x,y+1],[x,y+2]],   #
    lambda x, y: [[x,y],[x-1,y],[x-2,y],[x,y-1],[x,y-2]],   #
    ]

clrz = ["red", "blue", "yellow", "orange3", "green", "purple3"]
opaq = {"blue":"blue4", "red":"red3", "yellow":"yellow4", "orange3":"orange4", "green":"green4", "purple3":"purple4"}
flr = {"blue":"blue1", "red":"red1", "yellow":"yellow1", "orange3":"orange1", "green":"green1", "purple3":"purple1"}

blocks = [[None for i in range(8)] for i in range(8)]
score = 0
scalr = 1
last = 0
sincelast = 0

try:
    with open("blhs.txt", "r") as f:
        pass
except:
    with open("blhs.txt", "w") as f:
        f.write("0")

with open("blhs.txt", "r") as f:
    high = int(f.read())

hand = [random.choice(blckt), random.choice(blckt), random.choice(blckt)]
hc = [random.choice(clrz), random.choice(clrz), random.choice(clrz)]
ndx = 0
cqx = [True, True, True]
g_end = False


def valid(x, y):
    global ndx, blocks, hand

    construct = hand[ndx](x, y)
    insp = [item for item in list(set(sum(construct, []))) if (item<0 or item>7)]

    if insp==[]:
        vl = True

        for item in construct:
            if not blocks[item[0]][item[1]]==None:
                vl = False

    else:
        return False

    return vl


def check_end():
    global blocks, hand, cqx

    for q, ir in enumerate(hand):

        if not cqx[q] == False:

            for x in range(8):
                for y in range(8):

                    construct = ir(x, y)
                    insp = [item for item in list(set(sum(construct, []))) if (item<0 or item>7)]

                    if insp==[]:
                        vl = True

                        for item in construct:
                            if not blocks[item[0]][item[1]]==None:
                                vl = False

                    else:
                        vl = False

                    if vl==True:
                        return False
    return True



def place(state, x, y):
    global ndx, blocks, hand, hc, cells

    if not state==True:
        return None

    construct = hand[ndx](x, y)

    for item in construct:
        blocks[item[0]][item[1]] = hc[ndx]
        cells[item[1]][item[0]].cls(hc[ndx])

    gamereg()


def hover_ent(state, x, y):
    global ndx, cells, hand, hc, opaq, blocks, flr

    if not state==True:
        return None

    construct = hand[ndx](x, y)

    for item in construct:
        cells[item[1]][item[0]].cls(opaq[hc[ndx]])

    bl2 = __import__("copy").deepcopy(blocks)
    for item in construct:
        bl2[item[0]][item[1]] = hc[ndx]

    row, clm = [], []
    for i,item in enumerate(bl2):
        if None not in item:
            row.append(i)

    for i in range(8):
        if None not in [item[i] for item in bl2]:
            clm.append(i)

    for item in row:
        for i,row in enumerate(cells):
            cells[i][item].cls(flr[hc[ndx]])

    for item in clm:
        for i,row in enumerate(cells):
            cells[item][i].cls(flr[hc[ndx]])


def hover_lev(state, x, y):
    global ndx, cells, hand

    if not state==True:
        return None

    construct = hand[ndx](x, y)

    anim_blck()


def gamereg():
    global blocks, ndx, hc, hand, scalr, last, score, high, sincelast, cqx, g_end

    hand[ndx] = lambda x, y: []
    cqx[ndx] = False

    if cqx==[False, False, False]:

        hand = [random.choice(blckt), random.choice(blckt), random.choice(blckt)]

        if AI==True:
            mapgr = [[0 if i==None else 1 for i in item] for item in blocks]
            hand = blstai.select_optimal_pieces(mapgr, blckt)

        hc = [random.choice(clrz), random.choice(clrz), random.choice(clrz)]
        ndx = 0
        cqx = [True, True, True]


    row, clm = [], []
    for i,item in enumerate(blocks):
        if None not in item:
            row.append(i)

    for i in range(8):
        if None not in [item[i] for item in blocks]:
            clm.append(i)

    if row+clm==[]:
        sincelast+=1
        last = 0

        if sincelast>3:
            scalr = 1

    else:
        sincelast = 0
        scalr+=1
        last = len(row+clm)*10*scalr*2**len(row+clm)


    score+=last

    if score>high and AI==False:
        high = score

        with open("blhs.txt", "w") as f:
            f.write(str(high))

    for item in row:
        blocks[item] = [None for i in range(8)]

    for item in clm:
        for i,row in enumerate(blocks):
            blocks[i][item] = None

    g_end = check_end()
    glight(g_end)


    anim_optn()
    anim_blck()
    anim_gra()


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.sq = False
        self.col = "gray20"

        self.truex = int((x-10)/55)
        self.truey = int((y-100)/55)

        self.name = Button(root, bg=self.col, command = lambda: place(valid(self.truex, self.truey), self.truex, self.truey))

        self.name.bind("<Enter>", lambda event: hover_ent(valid(self.truex, self.truey), self.truex, self.truey))
        self.name.bind("<Leave>", lambda event: hover_lev(valid(self.truex, self.truey), self.truex, self.truey))

        self.name.place(x=self.x, y=self.y, height=55, width=55)

    def sqs(self, st):
        self.st = st

    def cls(self, col):
        self.col = col
        self.name['bg'] = self.col

    def gtr(self):
        return sq


class Graphic:
    def __init__(self, x, y, s=False, ns=None):
        self.x = x
        self.y = y

        self.name = Button(root, bg="black", command = None, state="disabled", borderwidth=0)

        if s==False:
            self.name.place(x=self.x, y=self.y, height=4, width=4)

        else:
            self.name.place(x=self.x, y=self.y, height=s, width=s)

        if not ns==None:
            self.name['command'] = lambda : setndx(ns)
            self.name['state'] = "normal"

    def yl(self):
        self.name['bg'] = "yellow"

    def bl(self):
        self.name['bg'] = "black"

    def cl(self, cl):
        self.name['bg'] = cl

    def brd(self, br):
        self.name['borderwidth'] = br


def setndx(q):
    global ndx, opn
    ndx = q

    for item in opn:
        item.bl()

    opn[ndx].yl()

def anim_optn():
    global optn, ndx, hc, hand, opn


    for item in optn:
        for i in item:
            for it in i:
                it.bl()
                it.brd(0)

    for i, it in enumerate(hand):
        construct = hand[i](2, 2)

        for item in construct:
            optn[i][item[1]][item[0]].cl(hc[i])
            optn[i][item[1]][item[0]].brd(1)

    for item in opn:
        item.bl()

    opn[ndx].yl()

def anim_gra():
    global graphcs, graphcz, high, score, scalr, last

    stsc = str(score).rjust(7, '0')

    for i,item in enumerate(stsc):
        for y in range(5):
            for x in range(3):
                graphcs[1+y][24+x+i*4].bl()


        for it in Alpha[item](24+i*4, 1):
            graphcs[it[1]][it[0]].yl()


    sthg = str(high).rjust(7, '0')

    for i,item in enumerate(sthg):
        for y in range(5):
            for x in range(3):
                graphcs[8+y][24+x+i*4].bl()


        for it in Alpha[item](24+i*4, 8):
            graphcs[it[1]][it[0]].yl()


    stscl = str(scalr).rjust(4, '0')

    for i,item in enumerate(stscl):
        for y in range(5):
            for x in range(3):
                graphcz[1+y][36+x+i*4].bl()


        for it in Alpha[item](36+i*4, 1):
            graphcz[it[1]][it[0]].yl()


    stlt = str(last).rjust(6, '0')

    for i,item in enumerate(stlt):
        for y in range(5):
            for x in range(3):
                graphcz[8+y][28+x+i*4].bl()


        for it in Alpha[item](28+i*4, 8):
            graphcz[it[1]][it[0]].yl()

def anim_blck():
    global blocks, cells

    for x,ir in enumerate(blocks):
        for y,ix in enumerate(ir):

            if ix==None:
                cells[y][x].cls("gray20")

            else:
                cells[y][x].cls(ix)

def restart():
    global blocks, score, scalr, last, sincelast, cqx, hc, ndx, hand, g_end

    blocks = [[None for i in range(8)] for i in range(8)]
    score = 0
    scalr = 1
    last = 0
    sincelast = 0
    hand = [random.choice(blckt), random.choice(blckt), random.choice(blckt)]
    hc = [random.choice(clrz), random.choice(clrz), random.choice(clrz)]
    ndx = 0
    cqx = [True, True, True]
    g_end = False
    glight(g_end)

    if AI==True:
        mapgr = [[0 if i==None else 1 for i in item] for item in blocks]
        hand = blstai.select_optimal_pieces(mapgr, blckt)

    anim_optn()
    anim_gra()
    anim_blck()

def rlight(m):
    global rb

    if m==False:
        rb['bg'] = "red1"
    else:
        rb['bg'] = "red4"

rb = Button(root, bg="red4", command=restart, text="Restart")
rb["font"] = tkFont.Font(family='Helvetica', size=int(14))
rb.bind("<Enter>", lambda event: rlight(False))
rb.bind("<Leave>", lambda event: rlight("haha"))

rb.place(x=150, y=670, height = 30, width=160)

gxe = Button(root, bg="dark olive green", state = "normal" , text="END?")
gxe["font"] = tkFont.Font(family='Helvetica', size=int(13))

gxe.place(x=386, y=684, height = 25, width=60)

def glight(m):
    global gxe

    if m==False:
        gxe['bg'] = "dark olive green"
    else:
        gxe['bg'] = "lawn green"

logo = [
Graphic(17,706), Graphic(18,702), Graphic(19,698), Graphic(20,694), Graphic(21,690),
Graphic(33,706), Graphic(34,702), Graphic(35,698), Graphic(36,694), Graphic(37,690),
Graphic(23,698), Graphic(27,698), Graphic(31,698),
Graphic(25,690), Graphic(29,690), Graphic(33,690),

Graphic(39,706), Graphic(40,702), Graphic(41,698),
Graphic(45,698),Graphic(49,698),

Graphic(53,706), Graphic(54,702), Graphic(55,698),
Graphic(57,706),
Graphic(61,706), Graphic(62,702), Graphic(63,698),

Graphic(67,706), Graphic(68,702), Graphic(69,698),
Graphic(73,698),
Graphic(75,706), Graphic(76,702), Graphic(77,698),


] + [Graphic(42+4*i,692) for i in range(10)]

for item in logo:
    item.cl("gray55")

cells = [[] for y in range(8)]

for y in range(8):
    for x in range(8):
        cells[y].append(Cell(10+x*55, 100+y*55))


graphcs = [[] for y in range(13)]
for y in range(13):
    for x in range(55):
        graphcs[y].append(Graphic(6+x*4, 6+y*4))

for item in Alpha["S"](1,1):
    graphcs[item[1]][item[0]].yl()
for item in Alpha["C"](5,1):
    graphcs[item[1]][item[0]].yl()
for item in Alpha["O"](9,1):
    graphcs[item[1]][item[0]].yl()
for item in Alpha["R"](13,1):
    graphcs[item[1]][item[0]].yl()
for item in Alpha["E"](17,1):
    graphcs[item[1]][item[0]].yl()
for item in Alpha[":"](21,1):
    graphcs[item[1]][item[0]].yl()

for item in Alpha["H"](13,8):
    graphcs[item[1]][item[0]].yl()
for item in Alpha["I"](17,8):
    graphcs[item[1]][item[0]].yl()
for item in Alpha[":"](21,8):
    graphcs[item[1]][item[0]].yl()


graphcz = [[] for y in range(13)]
for y in range(13):
    for x in range(55):
        graphcz[y].append(Graphic(227+x*4, 6+y*4))

for item in Alpha["S"](1,1):
    graphcz[item[1]][item[0]].yl()
for item in Alpha["C"](5,1):
    graphcz[item[1]][item[0]].yl()
for item in Alpha["A"](9,1):
    graphcz[item[1]][item[0]].yl()
for item in Alpha["L"](13,1):
    graphcz[item[1]][item[0]].yl()
for item in Alpha["R"](17,1):
    graphcz[item[1]][item[0]].yl()
for item in Alpha[":"](21,1):
    graphcz[item[1]][item[0]].yl()


for item in Alpha["L"](1,8):
    graphcz[item[1]][item[0]].yl()
for item in Alpha["A"](5,8):
    graphcz[item[1]][item[0]].yl()
for item in Alpha["S"](9,8):
    graphcz[item[1]][item[0]].yl()
for item in Alpha["T"](13,8):
    graphcz[item[1]][item[0]].yl()
for item in Alpha["+"](17,8):
    graphcz[item[1]][item[0]].yl()
for item in Alpha[":"](21,8):
    graphcz[item[1]][item[0]].yl()

opn = [Graphic(45, 555, s=110), Graphic(175, 555, s=110), Graphic(305, 555, s=110)]

optn = [[[] for y in range(5)], [[] for y in range(5)], [[] for y in range(5)]]

for i in range(3):
    for y in range(5):
        for x in range(5):
            optn[i][y].append(Graphic(50+x*20+i*130, 560+y*20, s=20, ns=i))

anim_optn()
anim_gra()


root.mainloop()
