import numpy as np
import sys
import matplotlib.pyplot as plt
from math import pi, cos, sin

def f(x):
    if x < 0:
        return 0
    else:
        return pi - x

def fourier(x, n):
    def An(n):
        return (1 - cos(pi*n))/(pi * n**2)

    def Bn(n):
        return (pi*n - sin(pi*n))/(pi * n**2)

    A0 = pi / 4
    ans = A0

    for i in range(1, n + 1):
        ans += An(i) * cos(i * x)
        ans += Bn(i) * sin(i * x)

    return ans

n = int(sys.argv[1]) if len(sys.argv) >= 2 else 15

x = np.linspace(-pi,pi,400)

y = [f(a) for a in x]
y_fourier = [fourier(a, n) for a in x]

plt.plot(x, y)
plt.plot(x, y_fourier)
plt.show()