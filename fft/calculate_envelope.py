# import peakutils
# from pylab import*
# from scipy.io import wavfile
# import matplotlib.pyplot as plt
# import wave
# import struct
#
#
# def wav_to_floats(wave_file):
#     w = wave.open(wave_file)
#     astr = w.readframes(w.getnframes())
#     # convert binary chunks to short
#     a = struct.unpack("%ih" % (w.getnframes()* w.getnchannels()), astr)
#     a = [float(val) / pow(2, 15) for val in a]
#     return a
#
#
# sampFreq, snd = wavfile.read('tracks/sample2.wav')
# signal = wav_to_floats('tracks/sample2.wav')
#
# print "read "+str(len(signal))+" frames"
# print "in the range "+str(min(signal))+" to "+str(min(signal))
#
#
# snd = snd / (2.**15)
#
# # print snd[:,0]
#
# s1 =  snd[:,0]
#
# # s1 = snd
# timeArray = arange(0, len(s1), 1)
# timeArray = timeArray / sampFreq
# timeArray = timeArray * 1000  #scale to milliseconds
# print timeArray.shape, s1.shape
# plt.plot(timeArray, s1, color='k')
# ylabel('Amplitude')
# xlabel('Time (ms)')
#
# # s1 = s1[1000:20000]
# # timeArray = timeArray[1000:20000]
# # plt.plot(timeArray, s1, 'k')
# indexes = peakutils.indexes(s1, thres=0.02/max(s1), min_dist=100000)
# # interpolatedIndexes = peakutils.interpolate(range(0, len(s1)), s1, ind=indexes)
# c = indexes.flatten()
# print timeArray.shape, s1[indexes].shape
# print
# # print indexes
# # print s1[indexes]
# plt.plot(timeArray[indexes], s1[indexes], 'bo')
# # plt.show()
# print 'end'
#
#
#
#
