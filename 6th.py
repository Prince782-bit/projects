from tkinter import *

win = Tk()
win.title("***** Digital Weather App *****")
win.config(bg = "blue")
win.geometry("500x500")

name_label = Label(win, text="__Weather_App__",font=("Time New Roman",20,"bold"))
name_label.place(x=25,y=30,height=30,width=450)





win.mainloop()