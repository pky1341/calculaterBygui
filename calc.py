import tkinter 

s=tkinter.Tk()
s.geometry('700x600')
s.title("simple calculater")
def add():
 x=int(n1.get())
 y=int(n2.get())
 res=x+y
 lres.config(text=str(x)+"+"+str(y)+"="+str(res))

def sub():
 x=int(n1.get())
 y=int(n2.get())
 res=x-y
 lres.config(text=str(x)+"-"+str(y)+"="+str(res))

def mult():
 x=int(n1.get())
 y=int(n2.get())
 res=x*y
 lres.config(text=str(x)+"*"+str(y)+"="+str(res))
def div():
 x=int(n1.get())
 y=int(n2.get())
 res=x/y
 lres.config(text=str(x)+"/"+str(y)+"="+str(res))
#lebel
l1=tkinter.Label(s,text='enter the first number  ',fg='green',font=("jokerman",20))
l1.place(x=50,y=50)
l2=tkinter.Label(s,text='enter the second no',fg='green',font=("jokerman",20))
l2.place(x=50,y=100)
lres=tkinter.Label(s,text="result",fg='green',font=("italic",20))
lres.place(x=50,y=150)
n1=tkinter.StringVar()
etry1=tkinter.Entry(s,bg="red",fg="white",font=("jokerman",20),textvariable=n1,bd=5)
etry1.place(x=350,y=50)
n2=tkinter.StringVar()
etry2=tkinter.Entry(s,bg="red",fg="white",font=("jokerman",20),textvariable=n2,bd=5)
etry2.place(x=350,y=100)
btn1=tkinter.Button(s,text="add",fg="blue",font=("jokerman",15),bd=5,command=add)
btn1.place(x=50,y=200)
btn2=tkinter.Button(s,text="sub",fg="blue",font=("jokerman",15),bd=5,command=sub)
btn2.place(x=150,y=200)
btn3=tkinter.Button(s,text="mult",fg="blue",font=("jokerman",15),bd=5,command=mult)
btn3.place(x=250,y=200)
btn4=tkinter.Button(s,text="div",fg="blue",font=("jokerman",15),bd=5,command=div)
btn4.place(x=350,y=200)
s.mainloop()
