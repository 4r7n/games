from tkinter import *
from random import *
from tkinter import messagebox


root=Tk()
root.geometry("300x300")
root.title("Aяυи")
root.resizable(False,False)
root.attributes('-topmost', 1)


pY3 = {"gd": 250000, "aq":31250, "mg":2000, "pk":686, "yl":250, "wt":128, "gr":54, "bl":31, "rd":16}
pY4 = {"gd": 33333333, "aq":2083333, "mg":53333, "pk":12805, "yl":3333, "wt":1365, "gr":432, "bl":208, "rd":85}

pR = {1:"gd", 3:"aq", 8:"mg", 15:"pk", 25:"yl", 38:"wt", 55:"gr", 75:"bl", 100:"rd"}

cL = {
     "rd" : "red2",
     "bl" : "medium blue",
     "gr" : "lawn green",
     "wt" : "MistyRose2",
     "yl" : "yellow",
     "pk" : "DeepPink2",
     "mg" : "magenta2",
     "aq" : "aquamarine",
     "gd" : "gold2"
     }

tY = ["rd", "bl", "gr", "wt", "yl", "pk", "mg", "aq", "gd"]

balance = 5000
bet = 10
notable, count = [], 0

class Slot:
    def __init__(self, x, y, cl):
        self.x = x
        self.y = y
        self.cl = cl

        self.item = Button(root, bg = cL[cl], command=None)

        self.item.place(x=x, y=y, height=30, width=30)

    def gt(self):
        return self.cl

    def st(self, nw):
        self.cl = nw
        self.item['bg'] = cL[nw]

def pr():
    num = randint(1,100)

    for item in pR:
        if num<=item:
            return pR[item]

tapes = [[] for i in range(3)]

for j,item in enumerate(tapes):
    for i in range(4):
        tapes[j].append(Slot(95 + 40*j, 90+30*i, pr()))


class Light:
    def __init__(self, x, y, h, w, name):
        self.item = Button(root, bg = "gray10", command=None, borderwidth=0, state='disabled')
        self.item.place(x=x, y=y, height=h, width=w)
        self.name = name

    def on(self):
        self.item['bg'] = 'LightBlue1'

    def off(self):
        self.item['bg'] = 'gray10'

    def gt(self):
        return self.name

Button(root, borderwidth=0, bg = "gray10", state='disabled').place(height=10,width=130, x=85, y=80)
Button(root, borderwidth=0, bg = "gray10", state='disabled').place(height=10,width=130, x=85, y=210)

lights = []
for i in range(3):
    lights.append(Light(95+40*i, 80, 10, 30, "4"+str(i)))
    lights.append(Light(95+40*i, 210, 10, 30, "4"+str(i)))

for i in range(4):
    lights.append(Light(85, 90+30*i, 30, 10, "3"+str(i)))
    lights.append(Light(125, 90+30*i, 30, 10, "3"+str(i)))
    lights.append(Light(165, 90+30*i, 30, 10, "3"+str(i)))
    lights.append(Light(205, 90+30*i, 30, 10, "3"+str(i)))

bal = Label(root, text="Balance:"+str(balance), font=("Helvetica", 10))
bal.place(x=0, y=0)

bt = Label(root, text="Bet:"+str(bet), font=("Helvetica", 10))
bt.place(x=0, y=20)

lw = Label(root, text="Last Spin: None", font=("Helvetica", 10))
lw.place(x=0, y=40)

def incr():
    global bet
    if not bet + int("1"+"0"*(len(str(bet))-1)) > balance:
        bet += int("1"+"0"*(len(str(bet))-1))
        bt['text'] = "Bet:"+str(bet)

def decr():
    global bet
    if not str(bet)[0]=="1":
        r = bet - int("1"+"0"*(len(str(bet))-1))
    else:
        r = bet - int("1"+"0"*(len(str(bet))-2))

    if r>=10:
        bet = r
        bt['text'] = "Bet:"+str(bet)


ic = Button(root, command=incr, bg="green1", text="+", font=("Helvetica", 20))
dc = Button(root, command=decr, bg="red", text="−", font=("Helvetica", 20))
ic.place(x=55,y=120, height=30, width =30)
dc.place(x=55,y=150, height=30, width=30)


def Iter(tape):
    tape[3].st(tape[2].gt())
    tape[2].st(tape[1].gt())
    tape[1].st(tape[0].gt())
    tape[0].st(pr())

def spin_anim():
    for i in range(100):
        Iter(tapes[0])

        if i>15:
            Iter(tapes[1])

        if i>30:
            Iter(tapes[2])

        root.after(1)
        root.update()

    for i in range(60):
        if i%3==0:
            Iter(tapes[0])

        if i>15:
            if i%2==0:
                Iter(tapes[1])
        else:
            Iter(tapes[1])

        if i>30:
            if i%3==0:
                Iter(tapes[2])
        else:
            Iter(tapes[2])

        root.after(1)
        root.update()


    for i in range(50):
        if i%7==0:
            Iter(tapes[0])

        if i>15:
            if i%7==0:
                Iter(tapes[1])
        else:
            if i%3==0:
                Iter(tapes[1])

        if i>30:
            if i%7==0:
                Iter(tapes[2])
        else:
            if i%3==0:
                Iter(tapes[2])

        root.after(1)
        root.update()

    for i in range(50):
        if i<20:
            if i%12==0:
                Iter(tapes[0])

        if i<35:
            if i>15:
                if i%12==0:
                    Iter(tapes[1])
            else:
                if i%7==0:
                    Iter(tapes[1])

        if i>30:
            if i%12==0:
                Iter(tapes[2])
        else:
            if i%7==0:
                Iter(tapes[2])

        root.after(1)
        root.update()




def spin():
    global balance, bet, notable, count

    if bet>balance:
        messagebox.showwarning("Error (you're broke)", "Bet is greater than balance, please try again.")

    else:
        spinner['state'] = "disabled"
        ic['state'] = "disabled"
        dc['state'] = "disabled"

        balance-=bet
        bal['text'] = "Balance:"+str(balance)

        count+=1


        for item in lights:
            item.off()

        spin_anim()

        win = 1
        wins = []

        for i,item in enumerate(tapes):
            if [it.gt() for it in item]==[item[0].gt() for ix in item]:
                win*=pY4[item[0].gt()]

                wins.append("4"+item[0].gt())

                for iz in lights:
                    if iz.gt()=="4"+str(i):
                        iz.on()

        for i,item in enumerate(tapes[0]):
            if [item.gt()] + [tapes[1][i].gt()] + [tapes[2][i].gt()] == [item.gt() for i in range(3)]:
                win*=pY3[item.gt()]

                wins.append("3"+item.gt())

                for iz in lights:
                    if iz.gt()=="3"+str(i):
                        iz.on()

        if win>1:
            balance += bet*win
            bal['text'] = "Balance:"+str(balance)
            lw['text'] = "Last Spin: "+str(bet*win)+" (x"+str(win)+")"

            wins.append(str(bet*win)+" (x"+str(win)+")")
            notable.append(wins)


        else:
            lw["text"] = "Last Spin: None"

        spinner['state'] = "normal"
        ic['state'] = "normal"
        dc['state'] = "normal"


spinner = Button(root, command=spin)
spinner.place(x=105,y=240,height=30,width=90)

auto = False

def at():
    global auto, ato

    if auto==False:
        auto = True
        ato['bg'] = 'LightBlue1'
        autobot()

    else:
        auto = False
        ato['bg'] = 'gray70'

def autobot():
    global bet, balance, auto

    if auto==True:

        bet = int("1"+"0"*(len(str(balance))-3))
        bt['text'] = "Bet:"+str(bet)

        spin()
        root.after(100, autobot)

ato = Button(root, command=at, bg="gray70", text ="Auto", font=("Helvetica", 9))
ato.place(x = 25, y = 120, height = 30, width = 30)

Button(root, command=(lambda: print(notable, count)), text = "Stats", font=("Helvetica", 9), bg="darkorchid").place(x = 25, y = 150, height = 30, width = 30)

root.mainloop()