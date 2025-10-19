import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

try:
    # 设置超时（10秒）
    socket.setdefaulttimeout(10)
    
    # 连接邮箱服务器
    print("正在连接QQ邮箱服务器...")
    qqMail = smtplib.SMTP_SSL("smtp.qq.com", 465, timeout=10)
    print("连接成功")
    
    mailUser = "2967124204@qq.com"
    mailPass = "tpscbphfxubtdcei"
    
    print("正在登录邮箱...")
    qqMail.login(mailUser, mailPass)
    print("登录成功")
    
    # 设置发件人和收件人
    sender = "2967124204@qq.com"
    receiver = "954340220@qq.com"
    
    print(f"发件人: {sender}")
    print(f"收件人: {receiver}")
    
    message = MIMEMultipart()
    message["Subject"] = Header("给大儿一封信")
    message["From"] = Header(f"dadie<{sender}>")
    message["To"] = Header(f"da er<{receiver}>")
    
    # 邮件正文
    textContent = "大儿 我帅不帅"
    mailContent = MIMEText(textContent, "plain", "utf-8")
    message.attach(mailContent)
    
    # 添加图片附件
    filePath = "C:/Users/MECHREVO/Desktop/下载.webp"
    print(f"正在读取附件: {filePath}")
    with open(filePath, "rb") as imageFile:
        fileContent = imageFile.read()
    
    attachment = MIMEImage(fileContent)
    attachment.add_header("Content-Disposition", "attachment", filename="大爹帅照.png")
    message.attach(attachment)
    print("附件添加成功")
    
    # 发送邮件
    print("正在发送邮件...")
    qqMail.sendmail(sender, receiver, message.as_string())
    print("发送成功！")
    
    # 关闭连接
    qqMail.quit()
    print("连接已关闭")
    
except smtplib.SMTPException as e:
    print(f"SMTP错误: {e}")
except socket.timeout:
    print("连接超时，请检查网络")
except Exception as e:
    print(f"发生错误: {e}")

# 添加这行，让程序等待用户输入后再退出
input("按回车键退出...")