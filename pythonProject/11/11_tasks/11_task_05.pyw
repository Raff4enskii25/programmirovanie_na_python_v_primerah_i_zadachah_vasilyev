# 5. Напишите программу, в которой отображается окно с шаблонным 
#текстом. Окно содержит две кнопки. При нажатии одной кнопки раз
#мер шрифта (которым отображается шаблонный текст) увеличивается 
#на единицу. При нажатии другой кнопки размер шрифта уменьшается 
#на единицу.
from tkinter import *
from tkinter import ttk

wnd=Tk()
wnd.title('Задание 5')
wnd.resizable(False,False)
wnd.geometry('400x150')

sz = IntVar()

fnt=('Calibri',sz.get(),'italic')

def increase():
    num = sz.get()
    if num<25:
        num+=1
        sz.set(num)

def decrease():
    num = sz.get()
    if num>1:
        num-=1
        sz.set(num)

def apply(*args):
    fnt=('Calibri',sz.get(),'italic')
    txt.configure(font=fnt)

txt = Label(wnd,text='Это текст для примера.',font=fnt)
increase_btn=Button(wnd,text='Увеличить',font=('Calibri',12,'bold'),command=increase)
decrease_btn=Button(wnd,text='Уменьшить',font=('Calibri',12,'bold'),command=decrease)
spinbox=ttk.Spinbox(wnd, from_=1,to=25,justify='right',textvariable=sz)
slider=Scale(wnd, orient=HORIZONTAL,from_=1,to=25, variable=sz)

txt.pack(side='top',fill='x',padx=5,pady=5)
increase_btn.pack(side='left',padx=5,pady=5)
decrease_btn.pack(side='left',padx=5,pady=5)
slider.pack(side='left',padx=5,pady=5)
spinbox.pack(side='left',padx=5,pady=5)

sz.trace('w',apply)
sz.set(15)

wnd.mainloop()