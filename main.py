from learn import learn
from predict import predict
from finch import Finch

# Finch has two modes, learn and predict
# In learn, the finch sets its wheels to the data points that it's most confused about to reduce confusion
# In predict, the finch tries to go forwards using current data

f_cor = input("Please enter the name of the file you want to save correct data to: ")
f_incor = input("Please enter the name of the file you want to save incorrect data to: ")

finch = Finch()

while True:
    user_in = input("e to exit, p to predict, l to learn: ").lower()
    if user_in == "p":
        predict(finch, f_cor, f_incor)
    elif user_in == "l":
        learn(finch, f_cor, f_incor)
    else:
        exit()
