import json
import sys
import matplotlib.pyplot as plt
import peakdetect
import hrvanalysis

def detect_r_peaks_ppg(y_axis, x_axis):
    #
    peaks = peakdetect.peakdetect(y_axis, x_axis,)
    return peaks


def csv_read(folder, csv_file, signal_type):
    s_type = ''
    if (signal_type == 'ppg'):
        s_type = 'pleth_1'
    if (signal_type == 'ecg'):
        s_type = 'ecg'
    with open(folder+csv_file) as file:
        lines = file.readlines()[:10001]
        head_line = lines[0]
        lines = lines[1:]
        head_args = head_line.split(',')
        signal = []
        peak = []
        peak_x = []
        #print("Peaks: ")
        for line in lines:
            values = line.split(',')
            signal_value = float(values[head_args.index(s_type)])
            signal.append(signal_value)
            peak_value = values[head_args.index('peaks')]
            #print(peak_value)
            if(peak_value.strip() == '1'):
                peak.append(signal_value)
                peak_x.append(lines.index(line)/500)
                #print(str(lines.index(line)/500) + 's : ' + str(signal_value))

        
    return signal, peak, peak_x

f_json = open('arguments.json')
  
data = json.load(f_json)

folder = data["csv_folder_path"]


arguments = sys.argv[1:]
csv_file = arguments[0]
signal_type = arguments[1]
signal, peak, peak_x = csv_read(folder, csv_file, signal_type)
num_of_elements = list(range(len(signal)))

#max_peak = 0
#
#for p in peak:
#    if p > max_peak:
#        max_peak = p

x_axis = []
for x in num_of_elements:
    x_axis.append(x/500)
#print(x_axis)


#r_peaks = []
#for r_p in r_peaks_times:
#    r_peaks.append(max_peak)

#print(len(peak_x))
#print(len(r_peaks_times))

plt.plot(x_axis, signal, color = 'green')
r_peaks_data = detect_r_peaks_ppg(signal, x_axis)

r_peaks_times = []
r_peaks_values = []

print("////////////")
print(r_peaks_data)
for i in range(len(r_peaks_data)):
    for rpd in r_peaks_data[i]:
        if(len(rpd) == 2):
            r_peaks_times.append(rpd[0])
            r_peaks_values.append(rpd[1])

rr_peaks_max = r_peaks_data[0]
rr_max_times = []
rr_max_values = []
for rr in rr_peaks_max:
    rr_max_times.append(rr[0])
    rr_max_values.append(rr[1])

print("////////////")
print(r_peaks_times)
print("////////////")
print(r_peaks_values)

plt.plot(peak_x, peak, 'ro')
plt.plot(r_peaks_times, r_peaks_values, 'bo')
plt.plot(rr_max_times, rr_max_values, 'yo')

nn_intervals = hrvanalysis.preprocessing.get_nn_intervals(rr_max_values, low_rri=80000, high_rri=100000)
print(nn_intervals)

time_domain_features = hrvanalysis.extract_features.get_time_domain_features(nn_intervals)
print(time_domain_features)

freq_domain_features = hrvanalysis.extract_features.get_frequency_domain_features(nn_intervals)
print(freq_domain_features)

poincare = hrvanalysis.extract_features.get_poincare_plot_features(nn_intervals)
print(poincare)

csi_cvi = hrvanalysis.extract_features.get_csi_cvi_features(nn_intervals)
print(csi_cvi)
#print(r_peaks_times)
#plt.plot(r_peaks, 'ro')
#print(r_peaks)
#plt.show()