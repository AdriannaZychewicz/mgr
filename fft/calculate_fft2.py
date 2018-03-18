#required libraries
import urllib
import scipy.io.wavfile
import pydub
import array
from pydub import AudioSegment
from pydub.utils import get_array_type
FFMPEG_BIN = "C:/ffmpeg-20180102-57d0c24-win64-static/bin"
#a temp folder for downloads
temp_folder="/Users/home/Desktop/"

#spotify mp3 sample file
web_file="C:/Users/azychewicz/PycharmProjects/untitled/tracks/audiocheck.net_sin_2000Hz_-3dBFS_3s.wav"


sound = AudioSegment.from_file(file=web_file)
left = sound.split_to_mono()[0]

bit_depth = left.sample_width * 8
array_type = get_array_type(bit_depth)

numeric_array = array.array(array_type, left._data)
#download file
urllib.urlretrieve(web_file,temp_folder+"file.mp3")
#read mp3 file
mp3 = pydub.AudioSegment.from_mp3(temp_folder+"file.mp3")
#convert to wav
mp3.export(temp_folder+"file.wav", format="wav")
#read wav file
rate,audData=scipy.io.wavfile.read(temp_folder+"file.wav")

print(rate)
print(audData)