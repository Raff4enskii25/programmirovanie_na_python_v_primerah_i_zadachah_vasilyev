# 3. Напишите программу, в которой отображается окно с полем ввода,
#  в которое следует ввести возраст пользователя. Программа должна 
#по возрасту (и текущему году) вычислить год рождения, который ото
# бражается в следующем диалоговом окне.
from tkinter import *
from datetime import datetime
wnd=Tk()
wnd.title('Задание 3')
wnd.geometry('450x200')
wnd.resizable(False,False)
wnd.configure(bg='white')

text = StringVar()
txt_yr = Label(text='Введите свой возраст:', font=('Arial',18,'bold'),bg='white')
txt_box = Entry(wnd, width=50,textvariable=text, font=('Arial',12,'italic'),relief=GROOVE)
frm_txt = Frame(wnd,bd=3,relief=GROOVE)
txt = Label(frm_txt,text='Вы ничего не ввели.',font=('Arial',18,'bold'),bg='white')

cur_year = datetime.now().year

txt_yr.pack(side='top', padx=10,pady=5)
txt_box.pack(side='top',padx=10,pady=15)
frm_txt.pack(side='top',padx=10,pady=15)
txt.pack()

def text_changed(*evt):
    try:
        if text.get()!="":
            age=eval(text.get())
            year=cur_year-age
            new_txt='Вы ' +str(year) +' года рождения.'
            txt.configure(text=new_txt)
        else:
            txt.configure(text='Вы ничего не ввели.')
    except Exception:
        txt.configure(text="Вы ввели не число!")

text.trace('w', text_changed)

wnd.mainloop()