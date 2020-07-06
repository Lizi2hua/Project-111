import json
import glob

# https://simpleitk.readthedocs.io/en/master/link_DicomConvert_docs.html
data_path=glob.glob('..\src\*.json')
# print(data_path)
for i in range(len(data_path)):
    json_dict=json.load(open(data_path[i]))
    json_data=json_dict['data']

