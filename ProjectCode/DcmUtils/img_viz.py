from json_read import get_info
from json_read import dicom2array
import matplotlib.pyplot as plt
train_path=r"C:\Users\Administrator\Desktop\lumbar\dataset\lumbar_train51\train"
json_path=r"C:\Users\Administrator\Desktop\lumbar\dataset\lumbar_train51\lumbar_train51_annotation.json"
#https://tianchi.aliyun.com/forum/postDetail?spm=5176.12586969.1002.12.46023a71FYtdgp&postId=113064

result=get_info(train_path,json_path)#图片路径以及标注
# print(result)
img_dir=result.index[0]#图片路径
img_arr=dicom2array(img_dir)
tags=result[0][0]['data']['point']#图片标签
# tag=tags[0]#第一个标签
# coord=tag['coord']#获取这个标签所在的坐标
#显示图片
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
#把这个图片所有的tags都加上去
for tag in tags:
    coord=tag['coord']
    top_left_x,top_left_y=coord[0]-7,coord[0]-7
    width,height=14,14
    rect=plt.Rectangle((top_left_x,top_left_y),width,height,fill=False,edgecolor='red',linewidth=1)
    ax.add_patch(rect)
plt.imshow(img_arr,cmap='gray')
plt.show()
