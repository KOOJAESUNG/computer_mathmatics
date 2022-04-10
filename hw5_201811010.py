import numpy as np
import matplotlib.pyplot as plt


def f(x):
    if np.abs(x) < 1:
        return 0
    if np.abs(x) > 1:
        return x
    if x == -1:
        return -0.5
    if x == 1:
        return 0.5


x = np.linspace(-2, 2, 401)
fx = np.zeros_like(x)

for i in range(0, 401):
    fx[i] = f(x[i])

plt.plot(x, fx, '.')
plt.show()
