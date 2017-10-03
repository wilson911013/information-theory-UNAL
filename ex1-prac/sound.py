import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wav
from scipy.fftpack import fft, fftfreq

rate, data = wav.read(sys.argv[1])

print(rate)

fft_out = fft(data)
frecs = fftfreq(len(data))
n = len(data)

plt.plot(frecs[:n//2], np.abs(fft_out)[:n//2])
plt.show()
