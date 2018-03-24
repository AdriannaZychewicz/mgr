import peakutils
from scipy import signal

import matplotlib.pyplot as plt

import numpy as np
#required libraries
import urllib
import scipy.io.wavfile
import pydub

#a temp folder for downloads
from env_fun.env_fun import get_envelope

temp_folder="/home/klichota/mgr-ada/mgr/tracks/mp3/converted/Guns_N_Roses_Welcome_To_The_Jungle.wav"
#read wav file
rate,audData=scipy.io.wavfile.read(temp_folder)


#create a time variable in seconds
time = np.arange(0, float(audData.shape[0]), 1) / rate

#wav number of channels mono/stereo
audData.shape[1]
#if stereo grab both channels
channel1=audData[:,0] #left
channel2=audData[:,1] #right

#plot amplitude (or loudness) over time
plt.figure(1)
# plt.plot(time, channel1, linewidth=0.05, alpha=0.8, color='r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
envelope = get_envelope(channel1)
plt.plot(time, envelope, linewidth=0.04, alpha=1, color='b')

w_cut = 10000
W1 = float(w_cut) / (float(rate))
(b, a) = signal.butter(4, W1, btype='lowpass')
# filtered_aver = signal.filtfilt(b, a, channel1)
# plt.plot(time, filtered_aver, linewidth=0.1, alpha=1, color='g')
filtered_aver = signal.filtfilt(b, a, envelope)
plt.plot(time, filtered_aver, linewidth=0.04, alpha=1, color='g')

indices = peakutils.indexes(filtered_aver, thres=0.678, min_dist=10)
plt.plot([j for j in range(len(filtered_aver))], filtered_aver, color='m',
        linewidth=0.06)
plt.plot(indices, [filtered_aver[j] for j in indices], color='k', linewidth=1)



plt.show()