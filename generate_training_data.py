import random

c = 0


while c < 50:
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    if a > 0.6 and abs(a - b) < 0.05:
        print(a, b)
        c += 1
"""

while c < 450:
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    if not (a > 0.6 and abs(a - b) < 0.05):
        print(a, b)
        c += 1
"""