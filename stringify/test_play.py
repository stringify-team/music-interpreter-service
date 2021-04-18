import sounddevice as sd
import soundfile as sf

filename = 'output.wav'

def play_sound(filename):
    """ plays sound from soundfile """
    # read from sound file
    data, fs = sf.read(filename, dtype='float32')

    # play from soundfile
    sd.play(data, fs)
    sd.wait()
    return

play_sound(filename)