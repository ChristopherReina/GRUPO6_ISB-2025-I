from opensignalsreader import OpenSignalsReader
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import iirdesign, filtfilt, freqz


archivos = ["BASAL.txt", "CONTRACCION_LEVE.txt", "CONTRACCION_FUERTE.txt"]

emg_signals = [None, None, None]

for i, archivo in enumerate(archivos):
    acq = OpenSignalsReader(archivo)
    emg_signals[i] = acq.signal("EMG")


fs = 1000  


wp_hz = 188 / (2 * np.pi)     
ws_hz = 300 / (2 * np.pi)     


Wp = wp_hz / (fs / 2)         
Ws = ws_hz / (fs / 2)         

gpass = 1    
gstop = 40   

b_butter, a_butter = iirdesign(wp=Wp, ws=Ws, gpass=gpass, gstop=gstop, ftype='butter')
b_cheby, a_cheby = iirdesign(wp=Wp, ws=Ws, gpass=gpass, gstop=gstop, ftype='cheby1')

w, h = freqz(b_butter, a_butter, worN=10000)
plt.figure()
plt.plot((w/np.pi)*(fs/2), 20*np.log10(abs(h)))
plt.title("Respuesta en frecuencia IIR (butter)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.show()

w, h = freqz(b_cheby, a_cheby, worN=10000)
plt.figure()
plt.plot((w/np.pi)*(fs/2), 20*np.log10(abs(h)))
plt.title("Respuesta en frecuencia IIR (chebyshev)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.show()

names = ["Basal", "Contracción leve", "Contracción fuerte"]

for i, signal in enumerate(emg_signals):
    x = signal
    t = np.arange(len(x)) / fs

    y_butter = filtfilt(b_butter, a_butter, x)
    y_cheby = filtfilt(b_cheby, a_cheby, x)

    plt.figure(figsize=(10, 12))

    plt.subplot(3, 2, 1)
    plt.plot(t, x, label=f"Señal original ({names[i]})")
    plt.grid()
    plt.legend()

    plt.subplot(3, 2, 2)
    plt.magnitude_spectrum(x, Fs=fs, label="Espectro original")
    plt.grid()
    plt.legend()

    plt.subplot(3, 2, 3)
    plt.plot(t, y_butter, label="IIR Butterworth")
    plt.grid()
    plt.legend()

    plt.subplot(3, 2, 4)
    plt.magnitude_spectrum(y_butter, Fs=fs, label="Espectro Butterworth")
    plt.grid()
    plt.legend()

    plt.subplot(3, 2, 5)
    plt.plot(t, y_cheby, label="IIR Chebyshev I")
    plt.grid()
    plt.legend()

    plt.subplot(3, 2, 6)
    plt.magnitude_spectrum(y_cheby, Fs=fs, label="Espectro Chebyshev I")
    plt.grid()
    plt.legend()
    plt.show()
