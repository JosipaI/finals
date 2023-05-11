import heartpy
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import networkx as nx
import pandas as pd
import wfdb
import csv

def detect_r_peaks_ppg(signal, sampling_rate):
    # Perform R-peak detection algorithm (e.g., using peak detection methods)

    # Replace the code below with your R-peak detection algorithm
    # For demonstration purposes, let's assume we have a simple threshold-based method
    threshold = 0.5  # Adjust the threshold as per your signal characteristics
    r_peaks = [i for i, val in enumerate(signal) if val > threshold]

    # Convert peak indices to timestamps
    r_peaks_timestamps = [i / sampling_rate for i in r_peaks]

    return r_peaks_timestamps


#current position of the database, move to .json file
record_name = '../../baza_2/physionet.org/files/pulse-transit-time-ppg/1.0.0/s1_run'  # Replace with the desired record name


#print(len(ppg_array))

record = wfdb.rdrecord(record_name)
annotation = wfdb.rdann(record_name, 'atr')

ppg_signal = record.p_signal[:1000, 0]  # Assuming PPG is the first channel
print(record.fs)


plt.plot(ppg_signal,  color ="green")


csv_file = '../../../baza_2/physionet.org/files/pulse-transit-time-ppg/1.0.0/csv/s1_run.csv'

peaks=[]
with open(csv_file, 'r') as file:
    lines = file.readlines()[1:1001]
    for line in lines:
        if line.split(',')[2] == '1':
            peaks.append(10000)
        else:
            peaks.append(0)

#print(peaks)
plt.plot(peaks, color='red')
plt.show()