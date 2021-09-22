from finch import Finch
from tkinter import *

finch = Finch()
main = Tk()
l = 0
r = 0


def up(event):
    l = 1
    r = 1

def down(event):
    l = -1
    r = -1

def left(event):
    l = -1
    r = 1

def right(event):
    l = 1
    r = -1

def updateFinch(event):
    finch.wheels(l, r)


frame = Frame(main, width=100, height=100)
main.bind('<Left>', left)
main.bind('<Right>', right)
main.bind('<Up>', up)
main.bind('<Down>', down)
frame.pack()
main.mainloop()
