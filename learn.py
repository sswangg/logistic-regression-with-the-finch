import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from finch import Finch
from random import uniform
from time import sleep
from sklearn.metrics import classification_report, confusion_matrix

# Finch has two modes, learn and predict
# In learn, the finch sets its wheels to the data points that it's most confused about to reduce confusion
# In predict, the finch tries to go forwards using current data

finch = Finch()

f_in1 = open("forward_data.txt", "r")
data1 = [[float(a) for a in s.split()] for s in f_in1.readlines()]
f_in1.close()
f_in2 = open("new_other_data.txt", "r")
data2 = [[float(a) for a in s.split()] for s in f_in2.readlines()]
f_in2.close()
data = data1+data2

# All wheel speed data
wheel_data_x = np.array([a for l in data for a in l]).reshape(-1, 2)
# 1s for going forwards, 0s for not
wheel_data_y = np.array([1 for i in data1]+[0 for j in data2])

model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(wheel_data_x, wheel_data_y)
print(model.predict(wheel_data_x))

zAccel = finch.acceleration()[2]

while zAccel > -0.7:
    w = [uniform(-1, 1), uniform(-1, 1)]
    print(w)
    finch.wheels(*w)
    is_right = input("Y if this movement is correct and N if not: ").lower() == "y"
    if is_right:
        forward
