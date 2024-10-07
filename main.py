from cmath import polar
from random import randint

import numpy as np
import random
import matplotlib.pyplot as plt



plt.figure("Yoi", figsize=(12, 7))


angles = np.linspace(0, 2 * np.pi, 1000)

r1= np.sin(111/122 * angles)


first = plt.subplot2grid((2, 2), (1, 0),polar=True)
first.set_yticklabels([]);

first.plot(angles, r1, linewidth=2, linestyle='-', color='r')

first.grid(False)

t = np.linspace(0, 2 * np.pi, 1000)
a = randint(1, 5)
b = randint(1, 5)
x1 = a * np.cos(t)
y1 = a * np.sin(2 * t) / 2

x2 = b * np.cos(t)
y2 = b * np.sin(2 * t) / 2

second = plt.subplot2grid((2, 2), (0, 1))
second.grid(True)

second.plot(x1, y1, linewidth=3, linestyle='--', color='b')
second.plot(x2, y2, linewidth=3, linestyle='--', color='g')

plt.show()
