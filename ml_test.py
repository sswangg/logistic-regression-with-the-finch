import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(x, y)
print(model.predict(x))


def data_to_scatter(file, color):
    f_in = open(file, "r")
    data = [[float(a) for a in s.split()] for s in f_in.readlines()[1:]]
    f_in.close()

    x_arr = np.array([t[0] for t in data])
    y_arr = np.array([t[1] for t in data])
    plt.scatter(x_arr, y_arr, color=color)


# Makes a plot showing data points that result in the robot going forwards in red and data points that result in the
# robot going a different direction in blue
data_to_scatter("forward_data.txt", "red")
data_to_scatter("other_data.txt", "blue")
plt.show()


