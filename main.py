from learn import learn
from predict import predict
from finch import Finch

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
