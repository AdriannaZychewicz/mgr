from pydub import AudioSegment
import matplotlib.pyplot as plt
import utils as utl

file = "tracks/Guns_N_Roses_Welcome_To_The_Jungle.mp3"

sound = utl.get_mp3(file)

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

print normalized_sound.max
print peak_amplitude
print sound.max_dBFS

plt.plot(samples_ch1)

