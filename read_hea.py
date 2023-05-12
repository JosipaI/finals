import sys
import json
import wfdb
import matplotlib.pyplot as plt

def hea_read(folder, atr_file):
    record_name = folder+atr_file
    record = wfdb.rdrecord(record_name=record_name)
    header = wfdb.rdheader(record_name)

    print(header.fs)
    print(header.base_counter)
    print(header.base_datetime)
    print(header.comments)
    

f_json = open("arguments.json")

data = json.load(f_json)
folder_path = data["folder_path"]

arguments = sys.argv[1:]

atr_file = arguments[0]


hea_read(folder_path, atr_file)
