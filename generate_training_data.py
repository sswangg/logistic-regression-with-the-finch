import random

c = 0
tolerance = 0.03


while c < 50:
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    if a > tolerance and abs(a - b) < 0.03:
        print(a, b)
        c += 1
"""

while c < 450:
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    if not (a > 0.6 and abs(a - b) < tolerance):
        print(a, b)
        c += 1
"""