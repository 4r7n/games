#MINES

from tkinter import *
from random import *

root=Tk()
root.geometry("400x450")
root.title("Aяυи")
root.resizable(False,False)
root.attributes('-topmost', 1)

balance, bet, remaining, current, new, multi = 10000, 100, 25, 1, 0, 1.0

def opened(item):
    global bet, remaining, current, end, mines, new, multi, mlt, cbt

    if item.stm("state")==False:
        new *= (remaining/(remaining - current))
        multi *= (remaining/(remaining - current))

        new = str(float(new))

        if int(new.split(".")[1])>0:
            new = int(float(new)) + 1

        else:
            new = int(float(new))

        #print(new, (remaining/(remaining - current)))

        if len(str(multi))>6:
            mlt['text'] = "Multi: "+str(multi)[:6]+"x"

        else:
            mlt['text'] = "Multi: "+str(multi)+"x"

        cbt['text'] = "Value: "+str(new)

        remaining -= 1


        item.stc("yellow")
        item.stt(False)

        if remaining==current:
            leave()

    else:
        end()

def start():
    global mines, current, end, remaining, balance, bet, leve, strt, new, mns, multi, mlt, cbt, bal, ic, dc

    if not bet>balance:
        remaining = 25
        multi = 1.0

        current = mns.get()

        balance -= bet

        new = bet

        for item in mines:
            item.stm(False)
            item.stc("SystemButtonFace")

        for item in sample(range(0,25), current):
            mines[item].stm(True)

        leve['state'] = "normal"
        strt['state'] = "disabled"
        mns['state'] = "disabled"

        ic['state'] = "disabled"
        dc['state'] = "disabled"

        mlt['text'] = "Multi: "+str(multi)+"x"
        cbt['text'] = "Value: "+str(new)
        bal['text'] = "Balance: "+str(balance)

        for item in mines:
            item.stt(True)

def leave():
    global balance, bet, leve, strt, mines, new, mns, bal, cbt, mlt, ic, dc

    balance+=new

    for item in mines:
        item.stt(False)

        if item.stm("state")==True:
            item.stc("red")

    leve['state'] = "disabled"
    strt['state'] = "normal"
    mns['state'] = "normal"

    ic['state'] = "normal"
    dc['state'] = "normal"

    mlt['text'] = "Multi: "
    cbt['text'] = "Value: "
    bal['text'] = "Balance: "+str(balance)


def end():
    global leve, mines, strt, mns, cbt, mlt, ic, dc

    for item in mines:
        item.stt(False)

        if item.stm("state")==True:
            item.stc("red")

    leve['state'] = "disabled"
    strt['state'] = "normal"
    mns['state'] = "normal"

    ic['state'] = "normal"
    dc['state'] = "normal"

    mlt['text'] = "Multi: "
    cbt['text'] = "Value: "



class Mine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mine = False

        self.item = Button(root, command = lambda: opened(self))
        self.item['state'] = 'disabled'

        #self.item.bind("<Button-2>", lambda event: dev(self))

        self.item.place(x=x, y=y, height=50, width=50)

    def stm(self, mne):
        if mne=="state":
            return self.mine

        else:
            self.mine = mne

    def stt(self, sta):
        if sta==True:
            self.item['state'] = 'normal'

        else:
            self.item['state'] = 'disabled'

    def stc(self, cl):
        self.item['bg'] = cl

    def ism(self):
        return(self.mine)


def dev(x):
    print(x.ism())


mines = []
for x in range(5):
    for y in range(5):
        mines.append(Mine(55 + x*60, 10 + y*60))

leve = Button(root, command = leave, text="Leave", state = "disabled", font=("Helvetica", 12))
leve.place(x = 50, y = 410, width = 70, height = 30)

strt = Button(root, command = start, text="Start", font=("Helvetica", 12))
strt.place(x = 50, y = 380, width = 70, height = 30)

def incr():
    global bet
    if not bet + int("1"+"0"*(len(str(bet))-1)) > balance:
        bet += int("1"+"0"*(len(str(bet))-1))
        bt['text'] = str(bet)

def decr():
    global bet
    if not str(bet)[0]=="1":
        r = bet - int("1"+"0"*(len(str(bet))-1))
    else:
        r = bet - int("1"+"0"*(len(str(bet))-2))

    if r>=10:
        bet = r
        bt['text'] = str(bet)


ic = Button(root, command=incr, bg="green1", text="+", font=("Helvetica", 20))
dc = Button(root, command=decr, bg="red", text="−", font=("Helvetica", 20))
ic.place(x=120,y=380, height=30, width =30)
dc.place(x=150,y=380, height=30, width=30)

bt = Button(root, text=str(bet), font=("Helvetica", 9))
bt.place(x=120, y=410, height=30, width = 60)

mns = Scale(root, label = "    Mines", font=("Helvetica", 11), orient=HORIZONTAL, from_=1, to=24)
mns.place(x=180, y = 380, height = 60, width = 90)

bal = Label(root, text="Balance: "+str(balance), font=("Helvetica", 11))
bal.place(x=55, y=305, height=20)

mlt = Label(root, text="Multi: ", font=("Helvetica", 11))
mlt.place(x=55, y=325, height=20)

cbt = Label(root, text="Value: ", font=("Helvetica", 11))
cbt.place(x=55, y=345, height=20)

root.mainloop()