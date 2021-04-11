from scipy.io.wavfile import write
import sounddevice as sd

fs = 44100
seconds = 3

def record_sound(sample_rate = 44100, seconds = 3, filename):
    """ reconds sound into numpy array and writes to file as wav """
    # record sound sample, wait for process to finish
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    # write to sound file
    write(filename, fs, myrecording)
    return

record_sound(sample_rate=fs, seconds=seconds, filename='output.wav')