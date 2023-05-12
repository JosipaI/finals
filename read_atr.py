import sys
import json
import wfdb
import matplotlib.pyplot as plt

def atr_read(folder, atr_file):
    record_name = folder+atr_file
    record = wfdb.rdrecord(record_name=record_name)
    annotation = wfdb.rdann(record_name=record_name, extension='atr')

    ecg = record.p_signal[:1000, 0]
    #print(annotation.get_label_fields())
    #print(annotation.symbol)
    
    return ecg, annotation.symbol

f_json = open("arguments.json")

data = json.load(f_json)
folder_path = data["folder_path"]

arguments = sys.argv[1:]

atr_file = arguments[0]

atr_file = arguments[0]
ecg, anno_symbol = atr_read(folder_path, atr_file)
for i in range(len(anno_symbol)):
    if(anno_symbol[i] != 'N'):
        print(anno_symbol[i] + ': ' + str(i))

plt.plot(ecg, color = 'green')
plt.show()