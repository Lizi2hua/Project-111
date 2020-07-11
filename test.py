# import json
# import glob
# import pydicom as idcom
#
# # https://simpleitk.readthedocs.io/en/master/link_DicomConvert_docs.html
# data_path=glob.glob('..\src\*.json')
# # print(data_path)
# # for i in range(len(data_path)):
# #     json_dict=json.load(open(data_path[i]))
# #     json_data=json_dict['data']
#
# idcom_path=r"C:\Users\李梓桦\Desktop\脊柱疾病检测\dataset\lumbar_train150\study10"
# idcom_path=glob.glob(idcom_path+'\*.dcm')
# print(idcom_path)
# for i in idcom_path:
#     img=idcom.read_file(i)
#     print(img)
#     print(type(img))
#     print(list(img)[0])
#     print("***********************")
#     # exit()
