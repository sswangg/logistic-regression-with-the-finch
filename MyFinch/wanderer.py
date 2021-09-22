# A simple program that wanders and avoids obstacles

from finch import Finch
from time import sleep

finch = Finch()

# Get the Z-Axis acceleration
zAccel = finch.acceleration()[2]

# Do the following while the Finch is not upside down (z value in gees above -0.7)
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
