import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

"""
x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(x, y)
print(model.predict(x))
"""


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
data = [[float(a) for a in s.split()] for s in f_in.readlines()[1:]]
f_in.close()
f_in = open("other_data.txt_data.txt", "r")
data += [[float(a) for a in s.split()] for s in f_in.readlines()[1:]]
f_in.close()

# All wheel speed data, 100 that go forwards then 1000 that don't
wheel_data_x = np.array([a for l in data for a in l]).reshape(-1, 2)
# 100 1s for going forwards, 1000 0s for not
wheel_data_y = np.array([1 for i in range(100)]+[0 for j in range(1000)])

model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(wheel_data_x, wheel_data_y)
print(model.predict(wheel_data_x))
