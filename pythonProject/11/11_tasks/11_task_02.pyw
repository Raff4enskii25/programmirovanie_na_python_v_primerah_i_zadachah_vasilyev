# 2. Напишите программу, в которой отображается окно с кнопкой и изображением.
#  При нажатии кнопки окно закрывается. При наведении курсора на область изображения
#  оно меняется на другое. Когда курсор покидает область изображения, оно меняется на исходное.
from tkinter import *
wnd=Tk()
wnd.title('Задание 2')
wnd.geometry('450x350')
wnd.resizable(False, False)
wnd.configure(bg='white')

files=['bad','good']
imgs=[]
for i in files:
    img = PhotoImage(file='D:\\Documents\\PythonTest\\pythonProject\\resources\\Pictures\\11_tasks\\11_02\\'+str(i)+'.png')
    imgs.append(img)

img_frm = Frame(wnd, bd=3, relief=GROOVE)
lbl=Label(img_frm, image=imgs[0])
btn=Button(wnd, text='Закрыть', font=('Arial',20,'bold'), command=wnd.destroy,relief=GROOVE)
img_frm.pack(side='top',fill='x',padx=5,pady=5)
lbl.pack(side='top',pady=5)
btn.pack(side='bottom',pady=5)

def ms_enter(evt):
    lbl.configure(image=imgs[1])
def ms_exit(evt):
    lbl.configure(image=imgs[0])

img_frm.bind("<Enter>", ms_enter)
img_frm.bind("<Leave>", ms_exit)

wnd.mainloop()
