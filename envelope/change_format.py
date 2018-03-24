#required libraries
import urllib

import os
import scipy.io.wavfile
import pydub

#a temp folder for downloads
temp_folder = "/home/klichota/mgr-ada/mgr/tracks/mp3"
converted_folder = '/home/klichota/mgr-ada/mgr/tracks/mp3/converted/'

for root, sub, files in os.walk(temp_folder):
    files = sorted(files)
    for f in files:
        w = os.path.join(root, f)
        filename, file_extension = os.path.splitext(f)
        mp3 = pydub.AudioSegment.from_mp3(w)
        base = os.path.basename(f)
        dir = os.path.dirname(base)
        converted = converted_folder + filename + ".wav"
        mp3.export(converted, format="wav")
        rate, audData = scipy.io.wavfile.read(converted)
        print(filename, rate)
        print'-------------------------'


