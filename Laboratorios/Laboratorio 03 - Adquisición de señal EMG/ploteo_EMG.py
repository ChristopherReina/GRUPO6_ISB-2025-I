#Importar librerias
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt  # Importar filtros

# Ruta donde están tus archivos .txt
folder_path = r"C:\Users\tulio\Desktop\EMG"

# Frecuencia de muestreo del BITalino (1000 Hz por defecto)
fs = 1000  

# Función para crear filtro pasa banda
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs  # Frecuencia de Nyquist
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

# Función del filtro
def bandpass_filter(data, lowcut=20, highcut=450, fs=1000, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# revisamos cada archivo .txt en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        # ignadar la cabecera inicial de los archivos .txt
        with open(file_path, 'r') as f:
            lines = f.readlines()
            start_idx = next(i for i, line in enumerate(lines) if 'EndOfHeader' in line) + 1

        # leer los datos como DataFrame
        df = pd.read_csv(file_path, delimiter='\t', skiprows=start_idx, header=None)
        df.columns = ["nSeq", "I1", "I2", "O1", "O2", "A1"]

        # Obtencion señal EMG
        emg = df["A1"].values.astype(float)

        # centrar la señal aplicando offset
        emg = emg - np.mean(emg)

        # normalizar
        emg = emg / np.max(np.abs(emg))

        # filtro pasa banda 20–450 Hz
        emg_filtrada = bandpass_filter(emg, lowcut=20, highcut=450, fs=fs)

        # crear tiempo
        t = np.arange(len(emg)) / fs

        # calcular FFT
        N = len(emg_filtrada)
        fft = np.fft.fft(emg_filtrada)
        fft = np.abs(fft[:N // 2])
        fft_db = 20 * np.log10(fft + 1e-6)
        freqs = np.fft.fftfreq(N, d=1/fs)[:N // 2]

        # estructura para mostrar los 2 graficos
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))

        # Ploteo señal EMG en el tiempo
        axs[0].plot(t, emg_filtrada, label="Señal filtrada", color='b')
        axs[0].set_xlabel("Tiempo (s)")
        axs[0].set_ylabel("Amplitud (mV)")
        axs[0].set_title(f"Señal EMG Filtrada - {filename}")
        axs[0].legend()

        # Ploteo FFT
        axs[1].plot(freqs, fft_db, color='r')
        axs[1].set_xlabel("Frecuencias (Hz)")
        axs[1].set_ylabel("Magnitud (dB)")
        axs[1].set_title("FFT en decibelios")
        axs[1].set_xlim(0, 200)  # puedes ajustar esto

        plt.tight_layout()
        plt.show()