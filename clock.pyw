from tkinter import *
from time import strftime

win = Tk()
win.title("Clock")
win.geometry('200x250')
win.resizable(0,0)
win.overrideredirect(True)
win.attributes("-transparentcolor","gray2")
win.config(bg="gray2")

def move_window(event):
    win.geometry('+{0}+{1}'.format(event.x_root,event.y_root))

def ext_but_vis(event):
    ext_but = Button(win,bg="Red",fg="White",text="X",command=quit,bd=0,activebackground="red3")
    ext_but.place(height=15,width=20,x=180,y=0)
    def end():
        ext_but.destroy()
    win.after(3000,end)

def time():
    date = strftime('%a  %d %B')
    Dt.config(text=date)
    hrs = strftime('%H')
    Hr.config(text=hrs)
    mintes = strftime('%M')
    Mn.config(text=mintes)
    Hr.after(1000,time)

Hr = Label(win,font=(None,60),fg="white",bg="gray2",cursor = "fleur")
Hr.pack(anchor ="center")
Mn = Label(win,font=(None,60),fg="white",cursor = "fleur",bg="gray2")
Mn.pack(anchor ="center")
Dt = Label(win,font=(None,16),fg="white",cursor = "fleur",bg="gray2")
Dt.pack(anchor ="center")
Hr.bind('<B1-Motion>',move_window)
Mn.bind('<B1-Motion>',move_window)
Dt.bind('<B1-Motion>',move_window)
Hr.bind("<Double-Button-1>",ext_but_vis)
Mn.bind("<Double-Button-1>",ext_but_vis)
Dt.bind("<Double-Button-1>",ext_but_vis)
time()
mainloop()
