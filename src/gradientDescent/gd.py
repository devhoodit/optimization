import matplotlib
import matplotlib.pyplot as plt
import numpy as np

func = lambda x: x**2
dfunc = lambda x: 2*x

def gd(x, dfunc, learning_rate=0.1):
    return x - learning_rate * dfunc(x)

x1 = 10

x = np.linspace(-10, 10, 2000)
y = np.array(func(x))

plt.plot(x, y)

for _ in range(10):
    x2 = gd(x1, dfunc)
    plt.plot([x1, x2], [func(x1), func(x2)], 'o-')
    x1 = x2


plt.show()