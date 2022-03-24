import matplotlib
import matplotlib.pyplot as plt
import numpy as np

func = lambda x: x**2
dfunc = lambda x: 2*x

def momentum(x, dfunc, v, a=0.9, learning_rate=0.1):
    v = a*v - learning_rate * dfunc(x)
    return x + v, v

x1 = 10
v = 0

x = np.linspace(-10, 10, 2000)
y = np.array(func(x))


plt.plot(x, y)

for _ in range(10):
    x2, v= momentum(x1, dfunc, v)
    plt.plot([x1, x2], [func(x1), func(x2)], 'o-')
    x1 = x2


plt.show()
