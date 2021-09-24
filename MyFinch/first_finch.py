from finch import Finch
import asyncio
import random
from tkinter import *

finch = Finch()
tk = Tk()
leftLight, rightLight = finch.light()
a=0
letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f'])
# 0.6019607843137255, 0.4666666666666667
notes_dict = {'a': 880,
         'b': 988,
         'c': 523,
         'd': 587,
         'e': 659,
         'f': 698}

def updateFinch(event):
    finch.wheels(slider1.get()/100.0,0)

tk.geometry("250x350")
slider1 = Scale(tk, from_=-100, to=100, label="Speed Left", orient='horizontal', command=updateFinch)
slider1.pack()

async def beak_control():
    leftLight, rightLight = finch.light()
    if (leftLight+rightLight)/2 < 0.55:
        finch.led(225,0,255)
    else:
        finch.led(0,0,0)

async def notes():
    global a, letter
    await asyncio.sleep(0.1)
    if a%10 == 0:
        letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f'])
    a += 1
    finch.buzzer(0.1, notes_dict[letter])

async def wander():
    zAccel = finch.acceleration()[2]
    while zAccel > -0.7:
        
        left_obstacle, right_obstacle = finch.obstacle()
        if left_obstacle and right_obstacle:
            finch.wheels(-1.0,-1.0)
            sleep(1.0)
            while left_obstacle:
                left_obstacle, right_obstacle = finch.obstacle()
            if not right_obstacle:
                finch.wheels(-0.3,-1.0)
                sleep(1.0)
            else:
                finch.wheels(-1.0, -0.3)
                sleep(1.0)
        elif left_obstacle:
            finch.led(255,0,0)
            finch.wheels(-0.3,-1.0)
            sleep(1.0)
            while left_obstacle:
                left_obstacle, right_obstacle = finch.obstacle()
        elif right_obstacle:
            finch.led(255,255,0)
            finch.wheels(-1.0, -0.3)
            sleep(1.0)
            while right_obstacle:
                left_obstacle, right_obstacle = finch.obstacle()
        else:
            finch.wheels(1.0, 1.0)
            finch.led(0,255,0)
        zAccel = finch.acceleration()[2]
        
    finch.close()

async def main():
    while True:
        L = await asyncio.gather(beak_control(), notes(), wander())

asyncio.run(main())
