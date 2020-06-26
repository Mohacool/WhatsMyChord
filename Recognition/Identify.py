import numpy as np
import matplotlib.pyplot as plt

# GLOBAL VARIABLES (TABLE OF NOTE FREQUENCIES)
noteTable = np.genfromtxt('note_frequency_table.csv', delimiter=',', encoding="utf-8-sig", dtype=None, invalid_raise = False, comments=None)
noteNames = np.array(noteTable[1:, 0])
noteFreqs = np.array(noteTable[1:, 1]).astype(float)


def freqToNote(freq):
    '''
    Given a frequency return the name of the note that is closest to the frequency provided, using this table of 
    frequencies of musical notes:
    
    https://www.liutaiomottola.com/formulae/freqtab.htm

    Function is vectorized, so it can be provided an array of frequencies at once
    '''
    
    # mean ratio between consecutive notes (technically all are equal, but we only have up to 3 decimals in table so ratios aren't exact)
    ratio = 1.0594634189848198
    
    # first note in the table:
    firstNote = 16.351
    
    # approximate index (rounded down) of freq in the table
    i = np.log(freq/firstNote)/np.log(ratio)

    freqDifference = np.array([np.abs(freq - noteFreqs[i.astype(int)]), np.abs(freq - noteFreqs[i.astype(int)+1])])

    possibleNotes = np.array([noteNames[i.astype(int)], noteNames[i.astype(int)+1]]).T  

    indices = (np.arange(freqDifference.shape[1]), np.argmin(freqDifference, axis=0))    


    note = possibleNotes[indices]
        
    return note


def Identify(qwe, sampFreq, thresh=3, drawPlots=False):
    '''
    Identifies the chord in the file with name fileName using Fourier analysis.
    
    Returns the list of notes in the chord
    '''
    
    # Find the amplitude of each frequency using fast fourier transform
    fft_spectrum = np.fft.rfft(qwe)
    amp = np.abs(fft_spectrum)
    freq = np.fft.rfftfreq(qwe.size, d=1./sampFreq)
    
    threshold = np.max(amp)/thresh
    
    # Plot the frequencies   
    if drawPlots:
        f1 = plt.figure()
        plt.plot(freq[:3500], amp[:3500])
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.title("Frequency spectrum")
        plt.plot(np.arange(1000), np.ones(1000)*threshold, label="threshold")
        plt.legend(loc="upper right")
        plt.savefig('freqSpectrum.png')
    
    
    # amplitudes that are above the threshold
    main_amp = np.where(amp>threshold, amp, 0)  # similar to amp, but amplitudes of all frequencies that are below the threshold are set to zero
    main_freqs = freq[np.argwhere(amp>threshold)][:, 0]

    
    
    #mainAmp is for plotting purposes only, we really only care about the argwhere
    # Plot the frequencies    
    if drawPlots:
        f1 = plt.figure()
        plt.plot(freq[:3500], main_amp[:3500])
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.title("Main frequencies in spectrum")
        plt.savefig('mainFreqs.png')
    
    all_chord_notes = freqToNote(main_freqs[:])
    chord_notes = set(all_chord_notes)
    
    
    return chord_notes
