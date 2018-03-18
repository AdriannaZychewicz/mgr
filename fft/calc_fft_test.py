import wave

import struct

import numpy as np

import matplotlib.pyplot as plt


frame_rate = 48000.0

infile = "C:\Users\azychewicz\PycharmProjects\untitled\tracks\audiocheck.net_sin_2000Hz_-3dBFS_3s.wav"

num_samples = 48000

wav_file = wave.open(infile, 'r')

data = wav_file.readframes(num_samples)

wav_file.close()

data = struct.unpack('{n}h'.format(n=num_samples), data)


data = np.array(data)

data_fft = np.fft.fft(data)

frequencies = np.abs(data_fft)

print("The frequency is {} Hz".format(np.argmax(frequencies)))

plt.subplot(2, 1, 1)

plt.plot(data[:300])

plt.title("Original audio wave")

plt.subplot(2, 1, 2)

plt.plot(frequencies)

plt.title("Frequencies found")

plt.xlim(0, 1200)

plt.show()