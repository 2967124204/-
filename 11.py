import pyautogui
import pyperclip
import time
import requests
import json
def openwechat():
    time.sleep(1)
    pyautogui.hotkey("ctrl","e")

def chatwho(name):  
    pyautogui.hotkey("ctrl","f")
    time.sleep(1)
    pyperclip.copy(name)
    pyautogui.hotkey("ctrl","v")
    time.sleep(1)
    pyautogui.hotkey("enter")
    time.sleep(1)
def sentmsg(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey("ctrl","v")
    time.sleep(1)
    pyautogui.hotkey("enter")
def getweather():
       url="https://weather.cma.cn/api/now/57679"
       header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"} 
       response=requests.get(url,headers=header)
       data=response.text
       data_json=json.loads(data) 
       city = data_json["data"]["location"]["name"]
       temp = data_json["data"]["now"]["temperature"]
       wind = data_json["data"]["now"]["windScale"]
       return f"亲爱的大儿，现在{city}的天气温度为{temp}度，有{wind}，好好照顾自己～"

openwechat()
chatwho("廖子乔")
sentmsg(getweather())




