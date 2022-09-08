import tkinter

s=tkinter.Tk()
s.geometry("600x300")
s.title("temperture calculater")
def ctof():
    f=eval(num.get())
    res=(f-32)*(5/9)
    l3.config(text=str(res))
def ftoc():
    c=eval(num.get())
    res=(9*c/5)+32
    l3.config(text=str(res))
l1=tkinter.Label(s,text="temprature calculater",font=("jokerman",20),fg="green",bg="yellow",bd=10)
l1.place(x=180,y=0)
l2=tkinter.Label(s,text="Enter Temprature:- ",font=("jokerman",20),fg="blue",bd=10)
l2.place(x=50,y=70)
l3=tkinter.Label(s,text="your Answer:-",font=("italic",20),bg="black",fg="red",bd=10)
l3.place(x=50,y=250)
num=tkinter.StringVar()
entry=tkinter.Entry(s,fg="blue",font=("italic",20),bd=10)
entry.place(x=300,y=70)
btn1=tkinter.Button(s,text="C  to   F",font=("italic",20),bg="cyan",fg="blue",bd=10,command=ctof)
btn1.place(x=100,y=150)
btn2=tkinter.Button(s,text="F  to   C",font=("italic",20),bg="cyan",fg="blue",bd=10,command=ftoc)
btn2.place(x=400,y=150)
s.mainloop()
