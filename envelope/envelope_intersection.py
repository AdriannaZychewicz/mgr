
# libraries
import numpy as np
import peakutils
import scipy
import os
import scipy.stats as stats

from scipy.io import wavfile
import wave, struct
import matplotlib.pyplot as pp

from pylab import *
import scipy.signal.signaltools as sigtool
import scipy.signal as signal
from scipy.fftpack import fft

# Here directory (put the name and path). Directory only with .wav files

# r_dir='/home/.../sound_files'
r_dir = '/home/klichota/mgr-ada/mgr/tracks/mp3/converted'

# Parameters

Fmax = 10000  # maximum frequency for the sonogram [Hz]
step_time = 60  # len for the time serie segment  [Seconds]->>>>>>>>> Change it to zoom in the signal time!!
w_cut = 800  # Frequency cut for our envelope implementation [Hz]
w_cut_simple = 150  # Frecuency cut for the low-pass envelope [Hz]


###################################
# 1) Function envelope with rms slide window (for the RMS-envelope implementation)

def window_rms(inputSignal, window_size):
    a2 = np.power(inputSignal, 2)
    window = np.ones(window_size) / float(window_size)
    return np.sqrt(np.convolve(a2, window, 'valid'))


##################################

# 2) Filter is directly implemented in Abs(signal)

##################################
# 3) our implementation !

def getEnvelope(inputSignal):
    # Taking the absolute value

    absoluteSignal = []
    for sample in inputSignal:
        absoluteSignal.append(abs(sample))

    # Peak detection

    intervalLength = 2  # change this number depending on your Signal frequency content and time scale
    outputSignal = []

    for baseIndex in range(0, len(absoluteSignal)):
        maximum = 0
        for lookbackIndex in range(intervalLength):
            maximum = max(absoluteSignal[baseIndex - lookbackIndex], maximum)
        outputSignal.append(maximum)

    return outputSignal


def moving_average(a, n=30) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def runningMeanFast(x, N):
    return np.convolve(x, np.ones((N,))/N)[(N-1):]


##################################
# Loop over sound files in directory

for root, sub, files in os.walk(r_dir):
    files = sorted(files)
    for f in files:
        w = scipy.io.wavfile.read(os.path.join(root, f))
        print r_dir
        base = os.path.basename(f)
        print base
        dir = os.path.dirname(base)

        a = w[1]
        print 'sound vector: ', w

        i = w[1].size

        print 'vector size in Frames: ', i

        x = w[1]
        x_size = x.size
        tt = w[1]

        # Comment for stero or not
        v1 = np.arange(float(i) / float(2))  # not stereo
        # v1    = np.arange(float (i))#/float(2)) #stereo
        c = np.c_[v1, x]

        print 'vector c:\n', c
        print 'vector c1:\n', c[0]

        cc = c.T  # transpose

        x = cc[0]
        x1 = cc[1]
        x2 = cc[1]  # 2

        print 'First cc comp:\n ', cc[0]
        print 'Second cc comp:\n', cc[1]
        print 'Third cc comp: \n', cc[1]  # cc[2] if stereo

        # Low Pass Frequency for Filter definition (envelope case 2)

        W2 = float(w_cut_simple) / (float(w[0]))  # filter parameter Cut frequency over the sample frequency
        (b2, a2) = signal.butter(1, W2, btype='lowpass')

        # Filter definition for our envelope (3) implementation

        W1 = float(w_cut) / (float(w[0]))  # filter parameter Cut frequency over the sample frequency
        (b, a) = signal.butter(4, W1, btype='lowpass')
        aa = scipy.signal.medfilt(scipy.signal.detrend(x2, axis=-1, type='linear'))
        i = x.size
        p = np.arange(i) * float(1) / float(w[0])

        stop = i
        step = int(step_time * float(w[0]))
        intervalos = np.arange(0, i, step)

        print intervalos
        print'-------------------'
        print'The step: ', step
        print'-------------------'

        time1 = x * float(1) / float(w[0])
        envelope_full = np.array([])
        time_full = np.array([])
        ##chop time serie##
        for delta_t in intervalos:
            aa_part = aa[delta_t:delta_t + step]
            x1_part = x2[delta_t:delta_t + step]  # or x1
            x2_part = x2[delta_t:delta_t + step]
            print delta_t
            # envelope our implementation
            # aver = getEnvelope(aa_part)
            # filtered_aver = signal.filtfilt(b, a, aver)
            # filtered_aver_part = filtered_aver[delta_t:delta_t + step]

            aver_vs = getEnvelope(x2_part)
            filtered_aver_vs = signal.filtfilt(b, a, aver_vs)
            # envelope_part = filtered_aver
            # filtered_aver_vs_part = filtered_aver_vs[delta_t:delta_t + step]

            # time (to x axis in seconds)

            time_part = time1[delta_t:delta_t + step]
            time = time1[delta_t:delta_t + step]

            ###################################################

            # # Figure definition
            # pp.figure(figsize=(14, 9.5 * 0.6))
            # pp.title('Sound Signal')
            # pp.subplot(2, 1, 1)

            # Uncoment what envelope you whant to plot

            # grid(True)
            cb = filtered_aver_vs
            indices = peakutils.indexes(cb, thres=0.678, min_dist=0.1)
            pp.plot([j for j in range(len(cb))], cb, color='b', label='Full envelope',
                    linewidth=1)
            pp.plot(indices, [cb[j] for j in indices], color='r', label='Full envelope', linewidth=2)
            plot_folder = '/home/klichota/mgr-ada/mgr/plots/envelope'
            fig_name = "%s.png" % (str(base) + '_signal_zoom_' + str(delta_t * float(1) / float(w[0])))
            pp.savefig(os.path.join(plot_folder, fig_name), dpi=200)
            pp.close('all')

            #FULL
            # envelope_full =np.append(envelope_full,filtered_aver_vs)
            # time_full = np.append(time_full,time_part)


            # pp.plot(time_part, filtered_aver_vs, color='r', label='Final Peak aproach  envelope', linewidth=2)
            #


            ##############################################################
            # save in plot file txt with data if necesary
            # data_dir = '/home/klichota/mgr-ada/mgr/data'
            # f_out = open(data_dir + '/%s.txt' %(str(base)+'_'+str(delta_t*float(1)/float(w[0]))), 'w')
            # xxx  = np.c_[time_part,x2_part,filtered_aver,filtered_aver_vs]
            # np.savetxt(f_out,xxx,fmt='%f %f %f %f',delimiter='\t',header="time   #sound   #sound-evelope   #vS-envelope")

        print '.---All rigth!!!----.'
        print time_full
        print envelope_full
        print envelope_full.shape
        pp.plot(time_full, envelope_full, color='r', label='Full envelope', linewidth=2)
        import pandas as pd
        import matplotlib.pyplot as plt

        # Plot the Raw Data

        # df = pd.DataFrame(envelope_full[0:1000])
        # smooth_data = df.rolling(200, win_type='gaussian')
        # ooth_data = df.rolling(200, win_type='gaussian')
        y1 = scipy.signal.medfilt(x2, 301)
        smooth_data2 = signal.hilbert(envelope_full)
        smooth_data = runningMeanFast(envelope_full, 10000)

        # envelope_full = envelope_full.tolist()
        # cb = np.array(envelope_full)
        # indices = peakutils.indexes(envelope_full, thres=0.678, min_dist=0.1)
        # x = indices
        # y = [envelope_full[j] for j in indices]
        # pp.plot(x, y, color='k', label='Full envelope', linewidth=2)
        # df = pd.DataFrame(data=envelope_full[1:, 1:])  # 1st row as the column names
        #pp.plot(time_full, smooth_data, color='b', label='Full envelope', linewidth=1)
        #pp.plot(time_full, y1, color='k', label='Full envelope', linewidth=2)
        #pp.show()

    import plotly.plotly as py
    import plotly.graph_objs as go
    from plotly.tools import FigureFactory as FF

    # import numpy as np
    # import scipy
    # import peakutils
    # cb = envelope_full
    # indices = peakutils.indexes(cb, thres=0.888, min_dist=0.1)
    # pp.plot([j for j in range(len(envelope_full))], envelope_full, color='b', label='Full envelope', linewidth=1)
    # pp.plot(indices, [envelope_full[j] for j in indices], color='r', label='Full envelope', linewidth=2)
    #
    #
    #
    # pp.show()
