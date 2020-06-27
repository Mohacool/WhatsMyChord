import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def plotSignal(signal, sampFreq):
    # Duration of the chord/sound (in seconds):
    duration = signal.shape[0] / sampFreq

    # To get the proper time on the x-axis we have to generate a numpy array using sampFreq:
    time = np.arange(signal.shape[0]) / signal.shape[0] * duration

    fig = plt.figure()
    plt.plot(time, signal)
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude")
    plt.title("Signal")
    plt.savefig('audio.png')