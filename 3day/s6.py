#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''def mail():
    n = 123
    y = 41324132
    b = n + y
    print(b)
    return 213
mail()
f = mail()
print(f)'''
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def mail(user):
    ret = True
    try:
        msg =  MIMEText('邮件内容','plain','utf-8')
        msg['From'] = formataddr(["贾强",'jiaq187@126.com'])
        msg['To'] = formataddr(["走人",'568784234@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.126.com",25)
        server.login("jiaq187@126.com","0802151523jia")
        server.sendmail('jiaq187@126.com',[user,],msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret
#return 1:返回值 2：中断操作
ret = mail('568784234@qq.com')

if ret:
    print("发送成功")
else:
    print("发送失败")

#断点查询 点击debug调试