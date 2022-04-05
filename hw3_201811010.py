import numpy as np
import matplotlib.pyplot as plt

# y=(log3(x))**2-log3(x**4)+3
x = np.linspace(0.1, 10, 1001)
y = (np.log(x) / np.log(3)) ** 2 - (np.log(x ** 4) / np.log(3)) + 3

# For visualization
plt.plot(x, y, label='$y=(log_3(x))^2-log_3(x^4)+3$')
plt.legend(loc='upper right')
plt.show()
