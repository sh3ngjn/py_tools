#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import yagmail
import pandas as pd
import random

# 编辑邮箱服务器
yag = yagmail.SMTP( user="xxxx@gmail.com", password="xxx", host='smtp.gmail.com', port='465')

# 读取联系人
contacts = pd.read_excel('/Users/username/Desktop/03-Project/01-工程开发/03-自动发邮件/contact.xlsx', engine='openpyxl')

# 更改联系人格式
address = contacts.values.tolist()
print(address)

# 在这里修改邮件主题
subject = ['今晚夜色真美', '小夜曲', 'hello，你好呀', '你好呀', '希望再次见到你']

# 发送邮件
for i, n in address:
    # 邮件正文
    content = [
        'hello {}'.format(i),
        '   午夜初眠梦见了你',
        '我从这美梦里醒来',
        # '/Users/svenj/Desktop/03-Project/01-工程开发/03-自动发邮件/1.jpeg', # 以附件形式发送
        yagmail.inline('/Users/username/Desktop/03-Project/01-工程开发/03-自动发邮件/pikachu.jpeg')# 内嵌图片
        ]
    # 随机邮件主题
    subject_send = random.choice(subject)
    yag.send(n, subject_send, content)
    print('have send to {}，the subject is {}'.format(i, subject_send))
yag.close()