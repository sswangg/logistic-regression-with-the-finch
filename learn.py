from finch import Finch
from random import uniform

# Finch has two modes, learn and predict
# In learn, the finch sets its wheels to the data points that it's most confused about to reduce confusion
# In predict, the finch tries to go forwards using current data

finch = Finch()

f_in1 = open("right.txt", "r")
data1 = [[float(a) for a in s.split()] for s in f_in1.readlines()]
f_in1.close()
f_in2 = open("wrong.txt", "r")
data2 = [[float(a) for a in s.split()] for s in f_in2.readlines()]
f_in2.close()

zAccel = finch.acceleration()[2]

while zAccel > -0.7:
    w = [uniform(-1, 1), uniform(-1, 1)]
    print(w)
    finch.wheels(*w)
    is_right = input("Y if this movement is correct and N if not: ").lower() == "y"
    if is_right:
        data1.append(w)
        f_in = open("right.txt", "w")
        f_in.write(str(data1))
        f_in.close()
    else:
        print(data2)
        data2.append(w)
        f_in = open("wrong.txt", "w")
        f_in.write("\n".join([" ".join([str(n) for n in d]) for d in data2]))
        f_in.close()
    zAccel = finch.acceleration()[2]

