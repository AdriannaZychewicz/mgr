from pydub import AudioSegment


def get_mp3(path):
    sound = AudioSegment.from_mp3(path)
    # sound._data is a bytestring
    return sound