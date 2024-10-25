from tkinter import *
from tkinter.ttk import Combobox
def change(evt):
    t=cb.get()
    for k in range(len(names)):
        if t==names[k]:
            lbl.configure(image=imgs[k])
            break
path="D:\\Documents\\PythonTest\\pythonProject\\resources\\Pictures\\11_04\\"
names=["Тигр","Лев",'Медведь']
files=['tiger.png','lion.png','bear.png']
wnd=Tk()
wnd.title('Хищники')
wnd.resizable(False, False)
wnd.geometry('220x300')
imgs=[PhotoImage(file=path+f) for f in files]
index=0
lbl=Label(wnd,image=imgs[index])
lbl.place(x=10,y=10,width=200,height=200)
cb=Combobox(wnd, state='readonly')
cb.configure(values=names)
cb.configure(font=(('Arial',11,'bold')))
cb.current(index)
cb.bind("<<ComboboxSelected>>",change)
cb.place(x=10,y=220,width=200,height=30)
btn=Button(wnd,text='OK', command=wnd.destroy)
btn.place(x=60,y=260,width=100,height=30)
wnd.mainloop()