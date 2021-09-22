from finch import Finch
from tkinter import *

finch = Finch()
tk = Tk()
leftLight, rightLight = finch.light()

def key(event):
    """shows key or tk code for the key"""
    if event.keysym == 'Escape':
        root.destroy()
    if event.char == event.keysym:
        # normal number and letter characters
        print( 'Normal Key %r' % event.char )
    elif len(event.char) == 1:
        # charcters like []/.,><#$ also Return and ctrl/key
        print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:
        # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( 'Special Key %r' % event.keysym )

def updateFinch(event):
    finch.wheels(slider1.get()/100.0,0)

tk.geometry("250x350")
slider1 = Scale(tk, from_=-100, to=100, label="Speed Left", orient='horizontal', command=updateFinch)
slider1.pack()

zAccel = finch.acceleration()[2]

