import wave
from wave import open
import struct
import scipy.io.wavfile as wavfile
import numpy as np

import matplotlib.pyplot as plt
from pydub import AudioSegment

# sound = AudioSegment.from_mp3("test.mp3")

FFMPEG_BIN = "C:/ffmpeg-20180102-57d0c24-win64-static/bin"

frame_rate = 48000.0

mp3 = AudioSegment.from_mp3("C:\\Users\\azychewicz\\PycharmProjects\\untitled\\tracks\\Guns_N_Roses_Welcome_To_The_Jungle.mp3")
mp3.export("C:\\Users\\azychewicz\\PycharmProjects\\untitled\\tracks\sample2.wav", format="wav")
print("The channels is {} ".format(np.argmax(mp3.frame_rate)))
mp3.frame_rate
infile = "C:\\Users\\azychewicz\PycharmProjects\untitled\\tracks\\sample2.wav"
#infile = "C:\\Users\\azychewicz\PycharmProjects\untitled\\tracks\\audiocheck.net_sin_2000Hz_-3dBFS_3s.wav"
sample_rate, data = wavfile.read(infile)

print sample_rate, data
num_samples = 48000

wav_file = wave.open(infile, 'r')

data = wav_file.readframes(num_samples)

wav_file.close()

# data = struct.unpack('{n}h'.format(n=num_samples), data)

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

plt.xlim(0, 50000)

plt.show()


