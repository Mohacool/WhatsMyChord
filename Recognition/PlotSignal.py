import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def plotSignal(asd, sampFreq):
    # Duration of the chord/sound (in seconds):
    duration = asd.shape[0] / sampFreq

    # To get the proper time on the x-axis we have to generate a numpy array using sampFreq:
    time = np.arange(asd.shape[0]) / asd.shape[0] * duration

    fig = plt.figure()
    plt.plot(time, asd)
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude")
    plt.title("Signal")
    plt.savefig('audio.png')

    asd = np.zeros(asd.shape)