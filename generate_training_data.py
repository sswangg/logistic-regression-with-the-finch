import random

c = 0
while c < 400:
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    if not (a > 0.6 and abs(a - b) < 0.1):
        print(a, b)
        c += 1
