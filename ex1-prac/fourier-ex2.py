from numpy import fft
import numpy as np
import matplotlib.pyplot as plt

n = 1000
dx = 5.0

x = dx*np.arange(0, n)

#Una senal de periodo T tiene frecuencia 2pi/T
w1 = 100.0
w2 = 20.0
fx = np.sin(2*np.pi*x/w1) + 2*np.cos(2*np.pi*x/w2)

Fk = fft.fft(fx)/n
nu = fft.fftfreq(n, dx)
Fk = fft.fftshift(Fk)
nu = fft.fftshift(nu)

_, plots = plt.subplots(3, 1, sharex=False)

plots[0].plot(nu, np.real(Fk))
plots[1].plot(nu, np.imag(Fk))
plots[2].plot(x, fx)

plt.show()