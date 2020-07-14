from torch.nn import Module
import torch.nn as nn
from torchvision.models import resnet50
import torch
from DataPreprocess import DataLabelGenerator
# model=resnet50(pretrained=False)
# para=model.parameters()
# print(next(iter(para)))
# modules=model.modules()
# print(next(iter(modules)))
# exit()
# coord:[[212, 43], [207, 59], [201, 81], [197, 98], [194, 118], [192, 138], [195, 157], [198, 178], [198, 196], [205, 210], [209, 232]]

class KpNet(Module):
    def __init__(self):
        super(KpNet,self).__init__()
        self.backbone=resnet50(pretrained=False)
        self.head=nn.Sequential(
            nn.Linear(1000,22)
        )

    def forward(self,x):
        out=self.backbone(x)
        return self.head(out)


DATA_PATH= r"C:\project\lumbar\Project-111\dataset\train_train51"
JSON_PATH= r"C:\project\lumbar\Project-111\dataset\train_train51/lumbar_train51_annotation.json"
idx=5
img_arr,coord,id,disc,vertebra=DataLabelGenerator(DATA_PATH,JSON_PATH,idx)
model=KpNet()
x=torch.Tensor([[img_arr,img_arr,img_arr],])
print(x)
pred=KpNet().forward(x)
print(pred)
#存在的问题：1，输入应该是3 channel而图像是1 channel
#         2. 输出是小数，而label是整数