import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.signal import find_peaks

def plot_wav_file_frequencies(filename):
    """ read from wav file and plots strongest sound frequencies """

    sampleFreq, myRecording = scipy.io.wavfile.read(filename)
    sampleDur = len(myRecording)/sampleFreq
    timeX = np.arange(0, sampleFreq/2, sampleFreq/len(myRecording))
    absFreqSpectrum = abs(fft(myRecording))
    print(absFreqSpectrum)
    print(absFreqSpectrum[200:])

    ymax = max(absFreqSpectrum)
    peaks, _ = find_peaks(absFreqSpectrum, height=20)
    print(peaks)

    print(absFreqSpectrum.argmax())
    xpos = absFreqSpectrum.argmax()
    print(timeX[peaks[0:2]])

    plt.plot(timeX, absFreqSpectrum[:len(myRecording)//2])
    plt.ylabel('|X(n)|')
    plt.xlabel('frequency[Hz]')
    plt.xlim([0, 5000])
    plt.show()
        
plot_wav_file_frequencies('output.wav')