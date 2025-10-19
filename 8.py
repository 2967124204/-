# 导入smtplib模块
import smtplib
# 从email.mime.multipart中导入MIMEMultipart类
from email.mime.multipart import MIMEMultipart
# 从email.header中导入Header类
from email.header import Header
# 从email.mime.text中导入MIMEText类
from email.mime.text import MIMEText
# 从email.mime.image中导入MIMEImage类
from email.mime.image import MIMEImage

# 连接邮箱服务器：使用smtplib模块的类SMTP_SSL，创建一个实例对象qqMail
qqMail = smtplib.SMTP_SSL("smtp.qq.com", 465)
# 设置登录邮箱的帐号为："aLing@qq.com"，赋值给mailUser
mailUser = "2967124204@qq.com"
# 将邮箱授权码"abcnawckdujkdace"，赋值给mailPass 
mailPass = "tpscbphfxubtdcei"
# 登录邮箱：调用对象qqMail的login()方法，传入邮箱账号和授权码
qqMail.login(mailUser, mailPass)

# 设置发件人和收件人
sender = "2967124204@qq.com"
receiver = "954340220@qq.com"
# 使用类MIMEMultipart，创建一个实例对象message
message = MIMEMultipart()
# 将主题写入 message["Subject"]
message["Subject"] = Header("给大儿一封信")
# 将发件人信息写入 message["From"]
message["From"] = Header(f"dadie<{sender}>")
# 将收件人信息写入 message["To"]
message["To"] = Header(f"da er<{receiver}>")

# 设置邮件的内容，赋值给变量textContent
textContent = "大儿 我帅不帅"
# 编辑邮件正文：使用类MIMEText，创建一个实例对象mailContent
mailContent = MIMEText(textContent, "plain", "utf-8")

# 将文件路径，赋值给filePath
filePath = "C:/Users/MECHREVO/Desktop/下载.webp"
# 使用with open() as语句以rb的方式，打开路径为filePath的图片，并赋值给imageFile
with open(filePath, "rb") as imageFile:
    # 使用read()函数读取文件内容，赋值给fileContent
    fileContent = imageFile.read()
# 设置邮件附件：使用类MIMEImage，传入参数fileContent，创建一个实例对象attachment
attachment = MIMEImage(fileContent)
# 调用add_header()方法，设置附件标题为"团队合照.png"
attachment.add_header("Content-Disposition", "attachment", filename="大爹帅照.png")

# 添加正文：调用对象message的attach()方法，传入正文对象mailContent作为参数
message.attach(mailContent)
# 添加附件：调用对象message的attach()方法，传入附件对象attachment作为参数
message.attach(attachment)

# 发送邮件：使用对象qqMail的sendmail方法发送邮件
qqMail.sendmail(sender, receiver, message.as_string())
# 输出"发送成功"
print("发送成功")