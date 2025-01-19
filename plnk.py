import turtle, math, random

turtle.hideturtle()
turtle.speed("fastest")
turtle.colormode(255)

turtle.tracer(0)

sc = turtle.Screen()
frame_delay_ms = 1000 // 120
frame = 0

count = 0
datafr = {1000:0, 130:0, 26:0, 9:0, 4:0, 2:0, 0.2:0, 0:0}
comp = 0
dev = False
stream = False

class Ball:
    def __init__(self, x, y, angle=0, type=None, m=1, v=0, value=0):
        self.x, self.y, self.m, self.angle, self.type = x, y, m, angle, type

        self.t = turtle.Turtle()
        self.t.hideturtle()

        self.value = value

        self.t.penup()
        self.t.shape("circle")
        self.t.speed("fastest")
        self.t.shapesize(1, 1)

        if type=="static":
            self.t.color("grey")
        else:
            self.t.color("red")

        self.t.goto(x, y)
        self.t.showturtle()

        self.time = 0
        self.rx = x
        self.ry = y
        self.v = v

        self.a = -9.8

    def getattr(self):
        return [self.x, self.y, self.v, self.m, self.angle, self.type, math.sqrt((self.v)**2 + (self.v + self.a*self.time)**2), self.value]

    def move(self):
        sx = self.v*self.time*math.cos(self.angle)
        sy = self.v*self.time*math.sin(self.angle) + 0.5*self.a*(self.time)**2

        self.x, self.y = self.rx + sx, self.ry + sy

        self.t.goto(self.x, self.y)
        self.time+=0.15

    def setattr(self, v, angle):
        self.time = 0
        self.rx, self.ry = self.x, self.y

        self.v, self.angle = v, angle

    def setcd(self, x, y):
        self.x = x
        self.y = y

        self.t.goto(x, y)


active = []
inactive = []

layers = 18
for i in range(2, layers):
    for j in range(i+1):

        inactive.append(Ball( (55)*(j-i/2) ,420-(45*i), type="static"))


class Win:
    def __init__(self, x, y, value, col):
        self.x, self.y, self.value, self.col = x, y, value, col

        self.t = turtle.Turtle()

        self.t.shapesize(1, 2.5)
        self.t.penup()
        self.t.shape("square")
        self.t.speed("fastest")

        self.t.goto(x, y)
        self.t.color(col)

        wrtr = turtle.Turtle()
        wrtr.hideturtle()
        wrtr.penup()
        wrtr.goto(x-25, y-30)

        wrtr.write("x"+str(value), move=False, align='left', font=('Arial', 14, 'normal'))
        wrtr.showturtle()
        wrtr.goto(x, y-40)
        wrtr.shape("square")
        wrtr.color(col)
        wrtr.shapesize(1, 2.5)

wins = []
vals = [1000, 130, 26, 9, 4, 2, 0.2, 0.2]+[0.2]+list(reversed([1000, 130, 26, 9, 4, 2, 0.2, 0.2]))
valscr = ["dark red", "red", "orange red", "tomato", "coral", "dark orange", "orange", "gold"]+["yellow"]+list(reversed(["dark red", "red", "orange red", "tomato", "coral", "dark orange", "orange", "gold"]))

for i,item in enumerate(vals):
    wins.append(Win((-480+i*60), -400, item, valscr[i]))


def detect(a, ia):
    ac, ic = list(map((lambda x: x.getattr()[:2]), a)), list(map((lambda x: x.getattr()[:2]), ia))

    for i, ax in enumerate(ac):
        for j,ix in enumerate(ic):
            if (ax[0] - ix[0])**2 + (ax[1] - ix[1])**2 <= 400:
                collision(a[i], ia[j])


def collision(t1, t2):
    clx = [(t1.getattr()[0] + t2.getattr()[0])/2, (t1.getattr()[1] + t2.getattr()[1])/2]

    A = math.atan2(t1.getattr()[1] - t2.getattr()[1], t1.getattr()[0] - t2.getattr()[0])

    u1, m1, a1, u2, m2, a2  = t1.getattr()[6], t1.getattr()[3], t1.getattr()[4], t2.getattr()[6], t2.getattr()[3], t2.getattr()[4]

    a1x = A
    a2x = (math.pi - A)/2

    v1 = u1*(math.sqrt(m1**2 + m2**2 + 2*m1*m2*math.cos(A))/(m1+m2))

    v2 = u1*(2*m1/(m1+m2))*math.sin(A/2)

    dist = math.sqrt((t1.getattr()[0] - t2.getattr()[0])**2 + (t1.getattr()[1] - t2.getattr()[1])**2)
    nx1 = clx[0] + 10 * (t1.getattr()[0] - t2.getattr()[0])/dist
    ny1 = clx[1] + 10 * (t1.getattr()[1] - t2.getattr()[1])/dist
    nx2 = clx[0] + 10 * (t2.getattr()[0] - t1.getattr()[0])/dist
    ny2 = clx[1] + 10 * (t2.getattr()[1] - t1.getattr()[1])/dist

    t1.setcd(nx1, ny1)
    t1.setattr(v1, a1x)

    t1.move()

queue = []

def tick():
    global queue, frame, active, lw, balance, bal, datafr, count, comp, dev, stream

    spwn = list(range(21,40))+list(range(-39,-20))

    for item in queue:
        active.append(Ball(random.choice(spwn), 410, value=item, v=1, angle=1.5*math.pi+random.normalvariate(sigma=0.2)))
    queue = []

    if dev == True:
        queue = [10]
        comp+=1

    for item in active:
        item.move()

    detect(active, inactive)

    for item in active:
        if item.getattr()[1]<-395:
            xcd = abs(item.getattr()[0])

            if xcd>505:
                datafr[0] += 1
                count+=1

            else:
                if xcd>455:
                    win = 1000
                elif xcd>405:
                    win = 130
                elif xcd>355:
                    win = 26
                elif xcd>305:
                    win = 9
                elif xcd>255:
                    win = 4
                elif xcd>205:
                    win = 2
                else:
                    win = 0.2

                balance+=win*item.getattr()[7]
                lw['text'] = "Last Spin: "+str(item.getattr()[7]*win)+" (x"+str(win)+")"
                bal['text'] = "Balance:"+str(balance)

                datafr[win] += 1
                count+=1

            active.remove(item)

    if stream==True:
        drop()

    if dev==True:
        tick()

    else:
        turtle.update()
        sc.ontimer(tick, frame_delay_ms)

        frame+=1

from tkinter import *

root=Tk()
root.geometry("200x90")
root.title("Aяυи")
root.resizable(False,False)
root.attributes('-topmost', 1)


balance = 5000
bet = 10

bal = Label(root, text="Balance:"+str(balance), font=("Helvetica", 10))
bal.place(x=30, y=0)

bt = Label(root, text="Bet:"+str(bet), font=("Helvetica", 10))
bt.place(x=30, y=20)

lw = Label(root, text="Last Win: None", font=("Helvetica", 10))
lw.place(x=30, y=40)

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
ic.place(x=0,y=0, height=30, width =30)
dc.place(x=0,y=30, height=30, width=30)

ic.bind("<Button-3>", lambda event: print(count, datafr, comp))
def dvstop(event):
    global dev
    dev = False
ic.bind("<Button-2>", dvstop)

def drop():
    global queue, balance, bet, stream

    if bet>balance and stream==False:
        messagebox.showwarning("Error (you're broke)", "Bet is greater than balance, please try again.")
    elif bet>balance and stream==True:
        pass

    else:
        queue.append(bet)
        balance -= bet
        bal['text'] = "Balance:"+str(balance)

drp = Button(root, command=drop, bg="gold", text="Bet", font=("Helvetica", 10))
drp.place(x=0,y=60, height=30, width=200)

def strtstrm(event):
    global stream
    if stream==False:
        stream = True
    else:
        stream = False

drp.bind("<Button-3>", strtstrm)

tick()
sc.mainloop()
root.mainloop()