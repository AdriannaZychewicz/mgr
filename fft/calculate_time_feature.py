from pydub import AudioSegment
import matplotlib.pyplot as plt
import utils as utl
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

# from envelope_test import getEnvelope


file = "/home/klichota/mgr-ada/mgr/tracks/vivaldi.mp3"

sound = utl.get_mp3(file)
def get_time_feature():
    loudness = sound.dBFS
    channel_no = sound.channels
    frame_rate = sound.frame_rate
    rms_value = sound.rms  # wartosc sredniokwadratowa (Root Mean Square)
    bytes_per_frame = sound.frame_width  #channels * sample_width
    peak_amplitude = sound.max
    duration = sound.duration_seconds
    normalized_sound = sound.apply_gain(-sound.max_dBFS)
    number_of_frames_in_sound = sound.frame_count()

    channel_data = AudioSegment.split_to_mono(sound)  # zwraca sygnal mono

    samples = sound.get_array_of_samples()     # from stereo
    samples_ch1 = channel_data[0].get_array_of_samples()
    samples_ch2 = channel_data[1].get_array_of_samples()
    test = np.average(list(filter(lambda x: x > 0, samples_ch1)))
    print normalized_sound.max
    print peak_amplitude
    print sound.max_dBFS

# plt.plot([test]*len(samples_ch1), 'r-')


def get_envelope(inputSignal):
    # Taking the absolute value

    absoluteSignal = []
    for sample in inputSignal:
        absoluteSignal.append(abs(sample))

    # Peak detection

    intervalLength = 5000  # change this number depending on your Signal frequency content and time scale
    outputSignal = []

    for baseIndex in range(0, len(absoluteSignal)):
        maximum = 0
        for lookbackIndex in range(intervalLength):
            maximum = max(absoluteSignal[baseIndex - lookbackIndex], maximum)
        outputSignal.append(maximum)

    return outputSignal


# plt.plot(samples_ch1)
# plt.plot([test]*len(samples_ch1), 'r-')
# plt.plot([0]*len(samples_ch1), 'g-')
# analytic_signal = hilbert(samples_ch1)
# amplitude_envelope = np.abs(analytic_signal)
# # plt.plot(amplitude_envelope)
# plt.plot(np.absolute(samples_ch1[10000:20000]))
# # plt.show()
# envelope = get_envelope(samples_ch1)
# # print( len(envelope))
# plt.plot(envelope, 'b-')
# plt.show()


file = "/home/klichota/mgr-ada/mgr/tracks/vivaldi.mp3"

sound = utl.get_mp3(file)
def get_signal(N):
    sound = utl.get_mp3(file)
    # sound_norm = sound.remove_dc_offset()
    channel_data = AudioSegment.split_to_mono(sound)  # zwraca sygnal mono
    samples = sound.get_array_of_samples()# from stereo
    max_amp = -abs(max(samples))
    samples = sound.get_array_of_samples()
    # norm = [x / max_amp for x in samples]

    samples_ch1 = channel_data[0].get_array_of_samples()
    print len(samples)
    samples_ch2 = channel_data[1].get_array_of_samples()
    normalized_sound2 = sound.apply_gain(-sound.max_dBFS)
    return samples_ch1[1:N]

print("poiuyt")


