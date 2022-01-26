
import requests
import tkinter as tk
import io
import json
def getJpg():

    # 获取金山词霸每日一句，英文和翻译
    url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    r = requests.get(url)
    content = r.text

    my_json = json.loads(content)
    #print(contents)
    return "https://cn.bing.com/"+ my_json["images"][0]["url"]

getJpg()


# # 下载图片数据
# image_bytes = requests.get(getJpg()).content
# # 将数据存放到data_stream中
# data_stream = io.BytesIO(image_bytes)
# # 转换为图片格式
# pil_image = Image.open(data_stream)

# tk_image = ImageTk.PhotoImage(pil_image)

import tkinter
 
win=tkinter.Tk()
photo=tkinter.PhotoImage(file="C:\Users\gongzhiqiang\Desktop\k.png")
label=tkinter.Label(win,image=photo)  #图片
label.pack()
win.mainloop()
