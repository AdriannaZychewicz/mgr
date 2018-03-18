import urllib
import scipy.io.wavfile
import pydub
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft as fft
import peakutils

mp3 = pydub.AudioSegment.from_mp3("tracks/Guns_N_Roses_Welcome_To_The_Jungle.mp3")
#convert to wav
mp3.export("tracks/file.wav", format="wav")
#read wav file
rate,audData=scipy.io.wavfile.read("tracks/file.wav")

print(rate)
# print(audData)
#wav length
audData.shape[0] / rate

#wav number of channels mono/stereo
audData.shape[1]
#if stereo grab both channels
channel1=audData[:,0] #left
channel2=audData[:,1] #right

print audData.dtype

#averaging the channels damages the music
mono=np.sum(audData.astype(float), axis=1)/2
#scipy.io.wavfile.write(temp_folder+"file2.wav", rate, mono)
#Energy of music
np.sum(channel1.astype(float)**2)

#power - energy per unit of time
1.0/(2*(channel1.size)+1)*np.sum(channel1.astype(float)**2)/rate

#create a time variable in seconds
time = np.arange(0, float(audData.shape[0]), 1) / rate
#plot amplitude (or loudness) over time
plt.figure(1)
# plt.subplot(211)
plt.plot(time, channel1, linewidth=0.1, alpha=1, color='#000000')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
indexes = peakutils.indexes(channel1, thres=0.02/max(channel1), min_dist=100)
plt.plot(time, indexes, linewidth=0.1, alpha=1, color='red')
# plt.subplot(212)
# plt.plot(time, channel2, linewidth=0.01, alpha=0.7, color='#ff7f00')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
plt.show()


from numpy import fft as fft

fourier=fft.fft(channel1)

plt.plot(fourier, color='#ff7f00')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.show()


fourier=fft.fft(channel1)
plt.figure(2)
plt.plot(fourier, color='#ff7f00')
plt.xlabel('k')
plt.ylabel('Amplitude')

n = len(channel1)
fourier = fourier[0:(n/2)]

# scale by the number of points so that the magnitude does not depend on the length
fourier = fourier / float(n)

#calculate the frequency at each point in Hz
# freqArray = np.arange(0, (n/2), 1.0) * (rate*1.0/n);
#
# plt.plot(freqArray/1000, 10*np.log10(fourier), color='#ff7f00', linewidth=0.02)
# plt.xlabel('Frequency (kHz)')
# plt.ylabel('Power (dB)')
#
# plt.show()



cb = np.array(channel1)
indexes = peakutils.indexes(channel1, thres=0.02/max(channel1), min_dist=100)

interpolatedIndexes = peakutils.interpolate(range(0, len(cb)), cb, ind=indexes)