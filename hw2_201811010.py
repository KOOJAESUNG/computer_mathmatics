import numpy as np
import matplotlib.pyplot as plt
def f(x):
    if x<=-1:
        return x+2
    if x>-1:
        return x**2

x = np.linspace(-5,5,1001)
fx = np.zeros_like(x)

for i in range(0,1001):
    fx[i] = f(x[i])
# y=f(x)의 그래프
plt.plot(x,fx,'.')
plt.show()