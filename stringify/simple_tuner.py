import sounddevice as sd
import numpy as np
import scipy.fftpack
import os


SAMPLE_FREQ = 44100 # sample frequency in Hz
WINDOW_SIZE = 44100 # window size of the DFT in samples
WINDOW_STEP = 21050 # step size of window
WINDOW_T_LEN = WINDOW_SIZE / SAMPLE_FREQ # length of the window in seconds
SAMPLE_T_LENGTH = 1 / SAMPLE_FREQ # length between two samples in seconds
window_samples = [0 for _ in range(WINDOW_SIZE)]


CONCERT_PITCH = 440
ALL_NOTES = ["A","A#","B","C","C#","D","Eb","E","F","F#","G","G#"]

def find_closest_note(pitch):
    """ finds closest note for a given pitch """

    i = int( np.round( np.log2( pitch/CONCERT_PITCH )*12 ) )
    closestNote = ALL_NOTES[i%12] + str(4 + np.sign(i) * int((9+abs(i))/12) )
    closestPitch = CONCERT_PITCH*2**(i/12)
    return closestNote, closestPitch


def callback(indata, frames, time, status):
    """ handles input sound data and prints closest note and pitch """
    global window_samples
    if status:
      print(status)
    if any(indata):
      window_samples = np.concatenate((window_samples,indata[:, 0])) # append new samples
      window_samples = window_samples[len(indata[:, 0]):] # remove old samples
      magnitudeSpec = abs( scipy.fftpack.fft(window_samples)[:len(window_samples)//2] )

      for i in range(int(62/(SAMPLE_FREQ/WINDOW_SIZE))):
        magnitudeSpec[i] = 0 #suppress mains hum

      maxInd = np.argmax(magnitudeSpec)
      maxFreq = maxInd * (SAMPLE_FREQ/WINDOW_SIZE)
      closestNote, closestPitch = find_closest_note(maxFreq)

      os.system('cls' if os.name=='nt' else 'clear')
      print(f"Closest note: {closestNote} {maxFreq:.1f}/{closestPitch:.1f}")
    else:
      print('no input')

# Start the microphone input stream
try:
    with sd.InputStream(channels=1, callback=callback,
      blocksize=WINDOW_STEP,
      samplerate=SAMPLE_FREQ):
      while True:
        pass
except Exception as e:
    print(str(e))