#presenter of the day
import tkinter
from PIL import ImageTk,Image
import random

s=tkinter.Tk()
s.geometry("500x400+100+100")
s.title("presenter of the day")
s.resizable(0,0)
names=["Elon Musk","Ratan Tata","bill gates","M.zukerberg","J.gosling"]
images=["am.png","rt.png","bg.png","mzb.png","jg.png"]
def play(lblp,lblname):
  n=random.randint(0,4)
  lblname.config(text=names[n])
  img=ImageTk.PhotoImage(Image.open(images[n]))
  lblp.config(image=img)
  lblp.image=img
  
lbl=tkinter.Label(s,text="presenter of the day",fg="blue",font=("Arial",20,"bold"))
lbl.place(x=100,y=20)
path="ap.png"
img=ImageTk.PhotoImage(Image.open(path))
lblp=tkinter.Label(s,image=img)
lblp.image=img
lblp.place(x=170,y=90)
lblname=tkinter.Label(s,text="Name",font=("Arial",18,"bold"),fg="blue")
lblname.place(x=170,y=280)
btn=tkinter.Button(s,text="play",font=("Times New Roman",20,"italic"),fg="blue",command=lambda:play(lblp,lblname))
btn.place(x=210,y=320)
s.mainloop()