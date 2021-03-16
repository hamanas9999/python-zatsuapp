from matplotlib import pyplot as plt
import numpy as np
import random

a = list(range(1, 21))
b = 0
l = []
while b < 20:
    l.append(random.randint(1, 100))
    b += 1

#x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#y = np.array([2, 6, 8, 4, 2, 15, 63, 58, 31, 41])

plt.plot(a, l)
plt.show()