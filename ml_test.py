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


def data_to_scatter(file, color):
    f_in = open(file, "r")
    data = [[float(a) for a in s.split()] for s in f_in.readlines()[1:]]
    f_in.close()

    x_arr = np.array([t[0] for t in data])
    y_arr = np.array([t[1] for t in data])
    plt.scatter(x_arr, y_arr, color=color)

    return np.array([a for l in data for a in l]).reshape(-1, 2)


# Makes a plot showing data points that result in the robot going forwards in red and data points that result in the
# robot going a different direction in blue
data_to_scatter("forward_data.txt", "red")
data_to_scatter("other_data.txt", "blue")
plt.show()

f_in = open("forward_data.txt", "r")
data1 = [[float(a) for a in s.split()] for s in f_in.readlines()]
f_in.close()
f_in = open("new_other_data.txt", "r")
data2 = [[float(a) for a in s.split()] for s in f_in.readlines()]
f_in.close()
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
    if model.predict(np.array(w).reshape(-1, 2)) > 0.7:
        finch.wheels(*w)
        sleep(1.0)
    zAccel = finch.acceleration()[2]
