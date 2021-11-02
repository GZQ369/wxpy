from tkinter import *
from tkinter import messagebox


def closeallroot():
    root.destroy()


def closeroot():
    messagebox.showinfo(title="警告", message="关不掉吧，气不气")
    return


def love(root):
    love = Toplevel(root)
    love.geometry("300x150+610+260")
    love.title("好巧啊，我也喜欢你")
    label = Label(love, text="如家酒店A350等你", font=("华文行楷", 25))
    label.pack()
    label = Label(love, text="电话给我，美滋滋", font=("华文行楷", 25))
    label.pack()

    entry = Entry(love, font=("楷体", 15))
    entry.pack()

    btn = Button(love, text="嗯嗯", width=10, height=2, command=closeallroot)
    btn.pack()
    love.protocol("WM_DELETE_root", closelove)


def closelove():
    messagebox.showinfo(title="好怂啊你", message="喜欢我直说就行")
    return


def noLove(root):
    no_love = Toplevel(root)
    no_love.geometry("300x100+610+260")
    no_love.title("我好喜欢你")
    label = Label(no_love, text="再考虑考虑呗", font=("华文行楷", 25))
    label.pack()
    btn = Button(no_love, text="好吧", width=10,
                 height=2, command=no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_root", closeNoLove)


def closeNoLove(root):
    messagebox.showinfo("不喜欢我，你就关不掉")
    messagebox.showinfo(title="警告", message="不喜欢我，你就关不掉")
    noLove(root)


# root = Tk()
# root.title("喜欢我么,来自一个漂亮女生的告白？")
# root.geometry("420x420+590+230")
# root.protocol("WM_DELETE_root", closeroot)

# label1 = Label(root, text="车佶，傻逼？气不气",
#                font=("华文行楷", 16), fg="red")
# label1.grid()
# label2 = Label(root, text="喜欢我么？", font=("华文行楷", 30))
# label2.grid(row=1, column=1, sticky=E)

# # photo=PhotoImage(file="./12345678/2.png")
# # imageLable=Label(root,image=photo)
# # imageLable.grid(row=2,columnspan=2)

# btn1 = Button(root, text="愿意", width=15, height=2, command=love)
# btn1.grid(row=3, column=0, sticky=W)

# btn2 = Button(root, text="不愿意", width=15, height=2, command=noLove)
# btn2.grid(row=3, column=1, sticky=E)


# root.mainloop()
