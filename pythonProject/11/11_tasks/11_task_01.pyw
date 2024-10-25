# 1. Напишите программу, в которой отображается окно с кнопкой,
# изображением и текстовой меткой. При нажатии кнопки окно закрывается.
from tkinter import *
wnd=Tk()
wnd.title('Задание 1')
wnd.geometry("450x350")
wnd.resizable(False, False)

img = PhotoImage(file="D:\\Documents\\PythonTest\\pythonProject\\resources\\Pictures\\11_tasks\\11_01\\image.png")
lbl = Label(wnd, text='Задание 1', font=('Times New Roman',12, 'bold'), image=img, compound='bottom')
lbl.pack(side='top',fill='x', pady=5)
btn=Button(wnd,text='Закрыть', font=('Calibri', 12, 'bold'), command=wnd.destroy, relief=GROOVE)
btn.pack(side='top',pady=5)

wnd.mainloop()