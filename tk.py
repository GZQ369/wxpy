# -*- coding: utf-8 -*-
import time, sys

from tkinter import *
from itchatwx import oneDayMsg
from anchor import *
mydelaymin = 3600 #窗口提示的延迟时间，以分钟计

#------------------def-------------------
def showMessage():
	#show reminder message window
	root = Tk()  #建立根窗口
	#root.minsize(500, 200)   #定义窗口的大小
	#root.maxsize(1000, 400)  #不过定义窗口这个功能我没有使用
	root.withdraw()  #hide window
	#获取屏幕的宽度和高度，并且在高度上考虑到底部的任务栏，为了是弹出的窗口在屏幕中间
	screenwidth = root.winfo_screenwidth()
	screenheight = root.winfo_screenheight() - 100 
	root.resizable(False,False)
	#添加组件
	root.title("喜欢我么？")
	root.iconbitmap('2.ico') #换icon

	frame = Frame(root, relief=RIDGE, borderwidth=3)
	frame.pack(fill=BOTH, expand=1) #pack() 放置组件若没有则组件不会显示
	#窗口显示的文字、并设置字体、字号
	label = Label(frame, text=oneDayMsg(), \
		font="Monotype\ Corsiva -20 bold")
	label.pack(fill=BOTH, expand=1)
	#按钮的设置
	button = Button(frame, text="嗯嗯", font="Cooper -25 bold", fg="black", command=root.destroy)
	button.pack(side=BOTTOM)


	root.update_idletasks()
	root.deiconify() #now the window size was calculated
	root.withdraw() #hide the window again 防止窗口出现被拖动的感觉 具体原理未知？
	root.geometry("{}x{}+{}+{}".format(root.winfo_width() + 10, root.winfo_height() + 10, 
	int((screenwidth - root.winfo_width())/2), int((screenheight - root.winfo_height())/2)))
	root.deiconify()
	root.protocol("WM_DELETE_WINDOW",closeroot)

	root.mainloop()
 
# showMessage()
 
 
while True:
	showMessage()
	time.sleep(mydelaymin*12) #参数为小时