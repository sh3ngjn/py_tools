import pandas as pd
import os.path
import os
import xlrd 

file_dir = "/Users/username/Desktop/公众号"

data_wechat = pd.DataFrame()

# for root_dir, sub_dir, files in os.walk(file_dir):
#     for file_name in os.listdir(root_dir):
#     # for file_name in os.listdir(os.path.join(root_dir, file_name))
#         if file_name.endswith((".xlsx", ".xls")):
#             file_name = os.path.join(root_dir, file_name).keys()
#             for i in file_name:
#                 print(i)

pathname = []

# 获取文件路径
for root_dir, sub_dir, files in os.walk(file_dir):
    for filename in files:
#         print(filename)
        if filename.endswith((".xlsx", ".xls")):
            pathname.append(os.path.join(root_dir, filename))
#             print(pathname)
print(pathname)  

# 读取数据
for i in pathname:
    print(i)
    print(pathname.index(i))
    # data = pd.read_excel(i, sheet_name="微信", usecols=['账号名', '粉丝量（万）', '头条品牌报价（元）'], engine='openpyxl')
    data = pd.read_excel(i, sheet_name="微信", usecols=lambda x: x.upper() in ['类别', '微信名称', 'ID', '粉丝数（万）', '平均阅读数', '头条刊例报价', '头条刊例报价', '税点', '折扣', '账期', '联系方式', '所属公司', '是否开通评论功能', '是否认证', '简介'], engine='openpyxl')
    print(data)
    data_wechat = pd.concat([data_wechat, data])
    print(data_wechat)
    
path2 = "/Users/username/Desktop/微信.xlsx"
writer = pd.ExcelWriter(path2, engine='openpyxl')
data_wechat.to_excel(writer, sheet_name="汇总微信公众号信息")
writer.save()
writer.close()
print('end')