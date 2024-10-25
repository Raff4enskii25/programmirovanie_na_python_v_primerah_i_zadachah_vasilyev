# 4. Напишите программу, в которой отображается окно с двумя кнопками,
# полем ввода и текстовой меткой. При вводе текста в текстовое 
#поле он автоматически дублируется в текстовой метке. Нажатие одной 
#из кнопок приводит к очистке поля и метки. Нажатие другой кнопки 
# приводит к закрытию окна
from tkinter import *
wnd=Tk()
wnd.resizable(False,False)
wnd.title('Задание 4')
wnd.geometry('350x250')

txt_box=Entry(wnd,font=('Times New Roman',14,'italic'),relief=GROOVE)
title_lbl=Label(wnd,text='Введите текст:',font=('Times New Roman',16,'bold'))
txt_frm=Frame(wnd,bd=3,relief=GROOVE)
result_lbl=Label(txt_frm,font=('Times New Roman',12,'bold'))
result_lbl.configure(text='Здесь будет ваш текст.')

def change_text():
    txt = txt_box.get()
    if txt!="":
        result_lbl.configure(text=txt)
    else:
        result_lbl.configure(text='Вы не ввели текст!')

btn_frm=Frame(wnd,bd=0)
change_btn=Button(btn_frm,text='Изменить',font=('Arial',14,'bold'),command=change_text)
close_btn=Button(btn_frm,text='Закрыть',font=('Arial',14,'bold'),command=wnd.destroy)

title_lbl.pack(side='top',fill='x',padx=5,pady=5)
txt_box.pack(side='top',fill='x',padx=5,pady=5)
btn_frm.pack(side='top',fill='x',padx=5,pady=5)
change_btn.pack(side='left',padx=30,pady=5)
close_btn.pack(side='right',padx=30,pady=5)

txt_frm.pack(side='top',fill='both',padx=5,pady=5,expand=True)
result_lbl.pack(side='top',fill='both',expand=True)

wnd.mainloop()
