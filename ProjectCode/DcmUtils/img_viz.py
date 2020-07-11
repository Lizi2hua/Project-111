from json_read import get_info
from json_read import dicom2array
import matplotlib.pyplot as plt
import os
import cv2

train_path=r"C:\project\lumbar\Project-111\dataset\train_train51"
json_path=r"C:\project\lumbar\Project-111\dataset\train_train51\lumbar_train51_annotation.json"
# train_path=r"C:\Users\Administrator\Desktop\lumbar\dataset\lumbar_train51\train"
# json_path=r"C:\Users\Administrator\Desktop\lumbar\dataset\lumbar_train51\lumbar_train51_annotation.json"
#https://tianchi.aliyun.com/forum/postDetail?spm=5176.12586969.1002.12.46023a71FYtdgp&postId=113064

result=get_info(train_path,json_path)#图片路径以及标注
# tags=result[i]#图片的标注信息
COORD=[]
VERTEBRA=[]
DISC=[]
ID=[]
for i in range(len(result)):
    tags=result[i] #tags 是个列表
    # print(tags)
    data=tags[0]['data'] # tags[0]是一个字典，使用字典索引
    point=data['point']
    print(point)
    # tags
    coord=[]
    vertebra=[]
    disc=[]
    id=[]
    for j in range(len(point)):
        coord_list=point[j]['coord']#point是一个列表，使用切片索引
        coord.append(coord_list)#[[169, 252], [169, 224], [171, 194], [172, 161], [175, 126], [171, 270], [169, 238], [171, 209], [171, 175], [172, 145], [176, 108]]
        id_=point[j]['tag']['identification']
        id.append(id_)
        name=point[j]['tag']
        vertebra_=name.get('vertebra')
        vertebra.append(vertebra_)#['v2', 'v2', 'v2', 'v2', 'v2', None, None, None, None, None, None]
        disc_=name.get('disc')
        disc.append(disc_)#[None, None, None, None, None, 'v3', 'v2', 'v3', 'v2', 'v5', 'v5']
    COORD.append(coord)#
    ID.append(id)
    VERTEBRA.append(vertebra)
    DISC.append(disc)
# print('id')
# print(ID)
# print('coord')
# print(COORD)
# print('vertebra')
# print(VERTEBRA)
# print('disc')
# print(DISC)
# exit()
# 用cv2画点
plt.ion()
for i in range(len(result)):
    img_dir=result.index[i]#图片路径
    print('图片{}路径'.format(i))
    print(img_dir)
    studyPath=os.path.split(img_dir)
    # print(studyPath)
    studyPath=os.path.split(studyPath[0])
    studyID=studyPath[1]
    # print(studyID)
    img_arr=dicom2array(img_dir)
    x=[]
    y=[]
    for j in range(len(COORD[i])):
        x1,y1=COORD[i][j]
        x.append(x1)
        y.append(y1)
    plt.title('{}‘s img'.format(studyID))
    plt.scatter(x,y,c='r',marker='+')
    plt.imshow(img_arr,cmap='gray')
    plt.show()
    plt.pause(1)
    plt.clf()
plt.ioff()


