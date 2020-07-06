import os
import json
import glob
import SimpleITK as sitk
import pandas as pd
from dcm_read import dicom_metainfo,dicom2array

train_path=r"C:\Users\李梓桦\Desktop\脊柱疾病检测\dataset\train"
json_path=r"C:\Users\李梓桦\Desktop\脊柱疾病检测\dataset\lumbar_train51_annotation.json"
# 文件路径配置的问题，将文件路径配置一下，还有将文件重新组织一下

annotation_info = pd.DataFrame(columns=('studyUid','seriesUid','instanceUid','annotation'))
json_df = pd.read_json(json_path)
# print(json_df)

for idx in json_df.index:
    studyUid = json_df.loc[idx,"studyUid"]
    seriesUid = json_df.loc[idx,"data"][0]['seriesUid']
    instanceUid =  json_df.loc[idx,"data"][0]['instanceUid']
    annotation =  json_df.loc[idx,"data"][0]['annotation']
    row = pd.Series({'studyUid':studyUid,'seriesUid':seriesUid,'instanceUid':instanceUid,'annotation':annotation})
    annotation_info = annotation_info.append(row,ignore_index=True)

dcm_paths = glob.glob(os.path.join(train_path,"**","**.dcm"))
# print(dcm_paths)
# 'studyUid','seriesUid','instanceUid'
tag_list = ['0020|000d','0020|000e','0008|0018']
dcm_info = pd.DataFrame(columns=('dcmPath','studyUid','seriesUid','instanceUid'))

# 有问题
for dcm_path in dcm_paths:
    # print(dcm_path)
    try:
        studyUid,seriesUid,instanceUid = dicom_metainfo(dcm_path,tag_list)
        print(studyUid)#有问题
        row = pd.Series({'dcmPath':dcm_path,'studyUid':studyUid,'seriesUid':seriesUid,'instanceUid':instanceUid })
        dcm_info = dcm_info.append(row,ignore_index=True)
        # print(row)
    except:
        continue
result = pd.merge(annotation_info,dcm_info,on=['studyUid','seriesUid','instanceUid'])
result = result.set_index('dcmPath')['annotation']
print(result)


