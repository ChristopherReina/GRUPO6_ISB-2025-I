from opensignalsreader import OpenSignalsReader
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import firwin, freqz, lfilter, filtfilt


archivos = ["BASAL.txt", "CONTRACCION_LEVE.txt", "CONTRACCION_FUERTE.txt"]

emg_signals = [None, None, None]

i = 0
for archivo in archivos:
    acq = OpenSignalsReader(archivo)
    emg_signal = acq.signal("EMG")
    emg_signals[i] = emg_signal
    i = i + 1
    
fs = 1000
fc = 40
N = 50

names = ["Basal", "Contracción leve", "Contracción fuerte"]
i = 0

b_hamming = firwin(numtaps=N, cutoff=fc, window="hamming", fs=fs)
b_blackman = firwin(numtaps=N, cutoff=fc, window="blackman", fs=fs)

w, h = freqz(b_hamming, worN=10000)
plt.figure()
plt.plot((w/np.pi)*(fs/2), 20*np.log10(abs(h)))
plt.title("Respuesta en frecuencia FIR (hamming)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.show()

w, h = freqz(b_blackman, worN=10000)
plt.figure()
plt.plot((w/np.pi)*(fs/2), 20*np.log10(abs(h)))
plt.title("Respuesta en frecuencia FIR (blackman)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.show()


for signal in emg_signals:

    x = signal
    t = np.arange(len(x)) / fs

    y_hamming_ff = filtfilt(b_hamming, 1, x)
    y_blackman_ff = filtfilt(b_blackman, 1, x)


    plt.figure(figsize=(10, 12))
    
    plt.subplot(3, 2, 1)
    plt.plot(t, x, label= f"Señal original ({names[i]})")
    plt.grid()
    plt.legend()
    
    plt.subplot(3, 2, 2)
    plt.magnitude_spectrum(x, Fs=fs, label= "Espectro de magnitud")
    plt.grid()
    plt.legend()

    plt.subplot(3, 2, 3)
    plt.plot(t, y_hamming_ff, label= "filtrado FIR hamming")
    plt.grid()
    plt.legend()

    plt.subplot(3, 2, 4)
    plt.magnitude_spectrum(y_hamming_ff, Fs=fs, label= "Espectro de magnitud")
    plt.grid()
    plt.legend()

    plt.subplot(3, 2, 5)
    plt.plot(t, y_blackman_ff, label= "filtrado FIR balckman")
    plt.grid()
    plt.legend()

    plt.subplot(3, 2, 6)
    plt.magnitude_spectrum(y_blackman_ff, Fs=fs, label= "Espectro de magnitud")
    plt.grid()
    plt.legend()
    plt.show()
    i = i + 1





