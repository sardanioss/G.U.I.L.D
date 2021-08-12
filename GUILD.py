import tkinter as tk
import ctypes
from PIL import Image, ImageTk

ctypes.windll.shcore.SetProcessDpiAwareness(1)


def placeholder():
    print("Your function comes here")


# Window Initialization
window = tk.Tk()
window.title("Window")
window.geometry("1250x625")
window.configure(bg = "#ffffff")


# Background of window (bg.png should be in same folder as this file)
img = Image.open("background.png")
bg_image = img.resize((int(img.width+(img.width*25/100)), int(img.height+(img.height*25/100))))
bg_image = ImageTk.PhotoImage(bg_image)
tk.Label(window, image=bg_image, borderwidth=0, relief="solid").place(x=0,y=0)


# Frame
tk.Frame(window, bg="#ffffff", width=1125, height=525).place(x=62, y=58)


# Text
tk.Label(window, text="GUI", font=("Comic Sans MS", 23), justify="left", bg="#FFFFFF",fg="#000000").place(x=72, y=58)


# Text
tk.Label(window, text="LD", font=("Comic Sans MS", 23), justify="left", bg="#FFFFFF",fg="#2b2bff").place(x=151, y=58)


# Text
tk.Label(window, text="WELCOME TO GRAPHICAL\nUSER INTERFACE\nLAYOUT DESIGNER", font=("Roboto", 23), justify="left", bg="#FFFFFF",fg="#000000").place(x=121, y=145)


# Text
tk.Label(window, text="Build eye pleasing GUI’s under minutes with\nsimple drag and drop interface of your\nproject without any hastle of debugging and\nmodifying code again and again!", font=("Courier New", 11), justify="left", bg="#FFFFFF",fg="#000000").place(x=121, y=342)


# Picutre (image should be in same folder as this file)
img_0 = Image.open("picture_0.png")
img_0 = img_0.resize((int(img_0.width+(img_0.width*25/100)), int(img_0.height+(img_0.height*25/100))))
pic_0 = ImageTk.PhotoImage(img_0)
tk.Label(window, image=pic_0, bg="#FFFFFF",borderwidth=0, relief="solid").place(x=705,y=123)


# Line
tk.Frame(window, width=1, height=415, bg="#000000").place(x=656, y=110)


# Text
tk.Label(window, text="Token ID:", font=("Roboto", 15), justify="left", bg="#3f3f3f",fg="#7e7e7e").place(x=755, y=210)


# Text
tk.Label(window, text="File  Link:", font=("Roboto", 15), justify="left", bg="#3f3f3f",fg="#7e7e7e").place(x=755, y=287)


# Entrybox
entrybox_0 = tk.Text(window, width=18, height=1, bg="#ffffff")
entrybox_0.place(x=901, y=216)


# Entrybox
entrybox_1 = tk.Text(window, width=18, height=1, bg="#ffffff")
entrybox_1.place(x=901, y=293)


# Button
img_b_0 = Image.open("button_0.png")
img_b_0 = img_b_0.resize((int(img_b_0.width+(img_b_0.width*25/100)), int(img_b_0.height+(img_b_0.height*25/100))))
pic_b_0 = ImageTk.PhotoImage(img_b_0)
button_0 = tk.Button(window, image = pic_b_0, activebackground="#3f3f3f", bg="#3f3f3f", relief="flat", command=lambda:[placeholder()])
button_0.place(x=828, y=396)
window.resizable(False, False)
window.mainloop()
