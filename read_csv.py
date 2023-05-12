import json
import sys
import matplotlib.pyplot as plt


def csv_read(folder, csv_file, signal_type):
    s_type = ''
    if (signal_type == 'ppg'):
        s_type = 'pleth_1'
    if (signal_type == 'ecg'):
        s_type = 'ecg'
    with open(folder+csv_file) as file:
        lines = file.readlines()[:4001]
        head_line = lines[0]
        lines = lines[1:]
        head_args = head_line.split(',')
        signal = []
        peak = []
        peak_x = []
        print("Peaks: ")
        for line in lines:
            values = line.split(',')
            signal_value = float(values[head_args.index(s_type)])
            signal.append(signal_value)
            peak_value = values[head_args.index('peaks')]
            #print(peak_value)
            if(peak_value.strip() == '1'):
                peak.append(signal_value)
                peak_x.append(lines.index(line)/500)
                print(str(lines.index(line)/500) + 's : ' + str(signal_value))

        
    return signal, peak, peak_x

f_json = open('arguments.json')
  
data = json.load(f_json)

folder = data["csv_folder_path"]

arguments = sys.argv[1:]
csv_file = arguments[0]
signal_type = arguments[1]
signal, peak, peak_x = csv_read(folder, csv_file, signal_type)
num_of_elements = list(range(len(signal)))
x_axis = []
for x in num_of_elements:
    x_axis.append(x/500)
print(x_axis)
plt.plot(x_axis, signal, color = 'green')
plt.plot(peak_x, peak, 'ro')
plt.show()