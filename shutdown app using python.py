from tkinter import *
import os

def restart():
    os.system("ShutDown /r /t 1")
def restart_time():
    os.system("ShutDown /r /t 20")
def LogOut():
    os.system("ShutDown /r /t -1")
def ShutDown():
    os.system("ShutDown /s /t 1")

st =Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")

r_button = Button(st,Text="Restart",font=("Time new roman",20,"bold"),
                  relief=RAISED,cursor="Plus",command=restart)
r_button.place(x=150,y=60,height=40,width=200)

rt_button = Button(st,Text="Restart Time",font=("Time new roman",20,"bold"),
                   relief=RAISED,cursor="Plus",command=restart)
rt_button.place(x=200,y=60,height=40,width=200)

rg_button = Button(st,Text="Log-Out",font=("Time new roman",20,"bold"),
                   relief=RAISED,cursor="Plus",command=LogOut)
rg_button.place(x=150,y=60,height=50,width=200)

rg_button = Button(st,Text="ShutDown",font=("Time new roman",20,"bold"),
                   relief=RAISED,cursor="Plus",command=ShutDown )
rg_button.place(x=150,y=370,height=50,width=200)

st.mainloop() # save the program