# 7. Напишите программу, в которой есть группа переключателей, предна
#значенная для выбора цвета. В окне отображается область, закрашенная 
#цветом, выбранным в группе переключателей
from tkinter import *
wnd=Tk()
wnd.resizable(False,False)
wnd.geometry('400x350')
wnd.title('Задание 7')

color=StringVar(value='green')
frm=Frame(wnd,bg='green',border=4,relief=GROOVE, width=200, height=200)
frm.pack(side='top',padx=5,pady=10)

def change_color(*args):
    frm.configure(bg=color.get())

green_rb=Radiobutton(wnd,text='Зеленый',value='green',variable=color)
green_rb.pack(side='left',padx=5,pady=5)
red_rb=Radiobutton(wnd,text='Красный',value='red',variable=color)
red_rb.pack(side='left',padx=5,pady=5)
blue_rb=Radiobutton(wnd,text='Синий',value='blue',variable=color)
blue_rb.pack(side='left',padx=5,pady=5)
yellow_rb=Radiobutton(wnd,text='Желтый',value='yellow',variable=color)
yellow_rb.pack(side='left',padx=5,pady=5)

color.trace('w',change_color)

wnd.mainloop()