from tkinter import *
from tkinter.messagebox import showinfo as showinfo

from random import sample

import time
strtd = 0
#147.76s

DIFF = 20
INCR = 25
ASPR = str(DIFF*INCR)+"x"+str(DIFF*INCR)
MINES = 50

root=Tk()
root.geometry(ASPR)
root.title("Aяυи")
root.resizable(False,False)
root.attributes('-topmost', 1)

from tkinter import font as tkFont
ft = tkFont.Font(family='Helvetica', size=int(INCR/2), slant='italic')

root.config(bg="navy")

start = True
revealed = []
win, grad = False, True

def clicked(x):
    global start, grid, revealed, mines, safe, selctd, win, strtd

    if start:
        strtd = time.time()

    if x.getAttr()[0]==True and start==False:
        for item in mines:

            if item.getAttr()[0]==True:
                item.nD()

        showinfo(title = "You Lost!", message=":(")
        root.destroy()

    if start==True and (x.getAttr()[0]==True or not x.getAttr()[3]==0):
        valid = False

        while not valid:
            for item in mines:
                item.detonate()

            selctd = sample(mines, MINES)
            crd = x.getAttr()[1:]

            for item in selctd:
                item.isMine()

            grid = []
            safe = []

            for item in mines:
                if item.getAttr()[0]==False:
                    safe.append(item)

            for i in range(DIFF):
                grid.append([])

            for item in grid:
                for i in range(DIFF):
                    item.append([])


            for item in mines:
                cd = item.getAttr()[1:]

                grid[cd[1]][cd[0]].append(item)


            for item in mines:
                if not item.getAttr()[0]==True:

                    cd = item.getAttr()[1:]
                    near = 0


                    #TOP LEFT
                    if not cd[0]==0 and not cd[1]==0:
                        if grid[cd[1]-1][cd[0]-1][0].getAttr()[0]==True:
                            near+=1

                    #TOP RIGHT
                    if not cd[0]==DIFF-1 and not cd[1]==0:
                        if grid[cd[1]-1][cd[0]+1][0].getAttr()[0]==True:
                            near+=1

                    #BOTTOM LEFT
                    if not cd[0]==0 and not cd[1]==DIFF-1:
                        if grid[cd[1]+1][cd[0]-1][0].getAttr()[0]==True:
                            near+=1

                    #BOTTOM RIGHT
                    if not cd[0]==DIFF-1 and not cd[1]==DIFF-1:
                        if grid[cd[1]+1][cd[0]+1][0].getAttr()[0]==True:
                            near+=1

                    #UP
                    if not cd[1]==0:
                        if grid[cd[1]-1][cd[0]][0].getAttr()[0]==True:
                            near+=1

                    #DOWN
                    if not cd[1]==DIFF-1:
                        if grid[cd[1]+1][cd[0]][0].getAttr()[0]==True:
                            near+=1

                    #LEFT
                    if not cd[0]==0:
                        if grid[cd[1]][cd[0]-1][0].getAttr()[0]==True:
                            near+=1

                    #RIGHT
                    if not cd[0]==DIFF-1:
                        if grid[cd[1]][cd[0]+1][0].getAttr()[0]==True:
                            near+=1

                    item.isNear(near)

            x = grid[crd[1]][crd[0]][0]

            if (not x.getAttr()[0]==True and x.getAttr()[3]==0):

                start = False
                valid = True
                break

    else:
        start = False

    def reveal(x):
        if x in revealed:
            return None

        #x.switch("disabled")

        if not x.getAttr()[3]==0:
            x.setTx(str(x.getAttr()[3]))
            if x.fl()==True:
                x.flag()
            revealed.append(x)

            return None

        else:
            cd = x.getAttr()[1:]
            x.dest()
            revealed.append(x)

            #TOP LEFT
            if not cd[0]==0 and not cd[1]==0:
                if not grid[cd[1]-1][cd[0]-1][0] in revealed:
                    reveal(grid[cd[1]-1][cd[0]-1][0])

            #TOP RIGHT
            if not cd[0]==DIFF-1 and not cd[1]==0:
                if not grid[cd[1]-1][cd[0]+1][0] in revealed:
                    reveal(grid[cd[1]-1][cd[0]+1][0])

            #BOTTOM LEFT
            if not cd[0]==0 and not cd[1]==DIFF-1:
                if not grid[cd[1]+1][cd[0]-1][0] in revealed:
                    reveal(grid[cd[1]+1][cd[0]-1][0])

            #BOTTOM RIGHT
            if not cd[0]==DIFF-1 and not cd[1]==DIFF-1:
                if not grid[cd[1]+1][cd[0]+1][0] in revealed:
                    reveal(grid[cd[1]+1][cd[0]+1][0])

            #UP
            if not cd[1]==0:
                if not grid[cd[1]-1][cd[0]][0] in revealed:
                    reveal(grid[cd[1]-1][cd[0]][0])

            #DOWN
            if not cd[1]==DIFF-1:
                if not grid[cd[1]+1][cd[0]][0] in revealed:
                    reveal(grid[cd[1]+1][cd[0]][0])

            #LEFT
            if not cd[0]==0:
                if not grid[cd[1]][cd[0]-1][0] in revealed:
                    reveal(grid[cd[1]][cd[0]-1][0])

            #RIGHT
            if not cd[0]==DIFF-1:
                if not grid[cd[1]][cd[0]+1][0] in revealed:
                    reveal(grid[cd[1]][cd[0]+1][0])

    reveal(x)

    v = True

    for item in selctd:
        if item.fl()==False:
            v = False
            break

    if v==True and len(revealed)==len(safe) and win==False:
        finish = str(time.time()-strtd)
        finish = finish.split(".")[0]+"."+finish.split(".")[1][:2]+"s"

        msg = "GG!\n\n" + finish

        showinfo(title = "You win!", message=msg)
        win = True

def flagged(x):
    global win, strtd

    if not (x in revealed and x.getAttr()[3]>0):
        x.flag()

    v = True

    for item in selctd:
        if item.fl()==False:
            v = False
            break

    if v==True and len(revealed)==len(safe) and win==False:
        finish = str(time.time()-strtd)
        finish = finish.split(".")[0]+"."+finish.split(".")[1][:2]+"s"

        msg = "GG!\n\n" + finish

        showinfo(title = "You win!", message=msg)
        win = True

def dev(x):
    global grad

    #print(x.getAttr())

    if grad == False:
        grad = True
        gradient()

    else:
        grad = False

class Mine:
    def __init__(self,x,y,bg,name):

        self.name = name
        self.text = name

        self.bg = bg
        self.fg = "red"
        self.flagged = False
        self.dir = True
        self.end = False

        self.x = x
        self.y = y

        self.mine = False
        self.near = 0


        self.name = Button(root, text=self.text, bg=self.bg, fg=self.fg, command = lambda: clicked(self))

        self.name["font"] = ft

        self.name.place(x=self.x, y=self.y, height=INCR, width=INCR)

        self.name.bind("<Button-3>", lambda event: flagged(self))

        self.name.bind("<Button-2>", lambda event: dev(self))

    def isMine(self):
        self.mine = True

    def detonate(self):
        self.mine = False

    def isNear(self,near):
        self.near = near

    def setTx(self,tx):
        self.name.config(text=tx)

    def setCol(self,bg):
        self.name.config(bg = bg)

    def switch(self,sw):
        self.name["state"] = sw

    def dest(self):
        self.name.destroy()
        mines.remove(self)

    def fl(self):
        return self.flagged

    def End(self):
        return self.end

    def nD(self):
        self.end = True
        self.name.config(bg="chartreuse")

    def rC(self):
        return [self.bg,self.dir]

    def sC(self,bg):
        self.bg = bg
        self.name.config(bg=self.bg)

    def dR(self,dr):
        self.dir = dr

    def sF(self,bg):
        self.bg = bg

    def flag(self):
        if self.flagged==False:
            self.name.config(bg="red")
            self.flagged = True

        else:
            self.name.config(bg=self.bg)
            self.flagged = False

    def getAttr(self):
        return [self.mine, int(self.x/INCR), int(self.y/INCR), self.near]


mines = []
safe = []

for x in range(DIFF):
    for y in range(DIFF):
        mines.append(Mine(x*INCR,y*INCR,"gray"+str(int(x*50/DIFF)+int(y*50/DIFF)),""))

selctd = sample(mines, MINES)

for item in selctd:
    item.isMine()

for item in mines:
    if item.getAttr()[0]==False:
        safe.append(item)

grid = []

for i in range(DIFF):
    grid.append([])

for item in grid:
    for i in range(DIFF):
        item.append([])


for item in mines:
    cd = item.getAttr()[1:]

    grid[cd[1]][cd[0]].append(item)


for item in mines:
    if not item.getAttr()[0]==True:

        cd = item.getAttr()[1:]
        near = 0


        #TOP LEFT
        if not cd[0]==0 and not cd[1]==0:
            if grid[cd[1]-1][cd[0]-1][0].getAttr()[0]==True:
                near+=1

        #TOP RIGHT
        if not cd[0]==DIFF-1 and not cd[1]==0:
            if grid[cd[1]-1][cd[0]+1][0].getAttr()[0]==True:
                near+=1

        #BOTTOM LEFT
        if not cd[0]==0 and not cd[1]==DIFF-1:
            if grid[cd[1]+1][cd[0]-1][0].getAttr()[0]==True:
                near+=1

        #BOTTOM RIGHT
        if not cd[0]==DIFF-1 and not cd[1]==DIFF-1:
            if grid[cd[1]+1][cd[0]+1][0].getAttr()[0]==True:
                near+=1

        #UP
        if not cd[1]==0:
            if grid[cd[1]-1][cd[0]][0].getAttr()[0]==True:
                near+=1

        #DOWN
        if not cd[1]==DIFF-1:
            if grid[cd[1]+1][cd[0]][0].getAttr()[0]==True:
                near+=1

        #LEFT
        if not cd[0]==0:
            if grid[cd[1]][cd[0]-1][0].getAttr()[0]==True:
                near+=1

        #RIGHT
        if not cd[0]==DIFF-1:
            if grid[cd[1]][cd[0]+1][0].getAttr()[0]==True:
                near+=1

        item.isNear(near)

def gradient():
    global grad

    for item in mines:
        [col,dr] = item.rC()

        if int(col.split("gray")[1])>=100:
            if dr==True:
                item.dR(False)

        elif int(col.split("gray")[1])<=0:
            if dr==False:
                item.dR(True)

        dr = item.rC()[1]

        if dr==True:
            nc = "gray"+str(int(col.split("gray")[1])+1)

        else:
            nc = "gray"+str(int(col.split("gray")[1])-1)


        if item.fl()==True or item.End()==True:
            item.sF(nc)

        else:
            item.sC(nc)

    if grad==True:
        root.after(4, gradient)

gradient()

root.mainloop()
