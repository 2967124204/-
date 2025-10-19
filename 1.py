#使用pillow制作照片墙
import PIL
from PIL import Image
img=Image.open("C:/Users/MECHREVO/Pictures/Screenshots/屏幕截图 2025-09-15 205834.png")
img_1=img.convert("1")#三通道(RGB)转换为单通道
newimg=img_1.resize((20,20))
#嵌套列表 
figure=[]
for i in range(20):
    row=[]
    for j in range(20):
        pix=newimg.getpixel((j,i))
        row.append(pix)
    print(row)
    figure.append(row)#将每一行值存储在列表figure中 嵌套列表
