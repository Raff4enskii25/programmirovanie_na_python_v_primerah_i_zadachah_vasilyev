#6. Напишите программу, в которой есть статический список с названия
#ми животных. При выборе пункта в статическом списке в окне отобра
#жается изображение выбранного животного.
from tkinter import *
from tkinter.ttk import Combobox
wnd=Tk()
wnd.geometry('450x350')
wnd.resizable(False,False)
wnd.title('Задание 6')

files=['fox.png','cat.png','dog.png','pig.png']
animals=['Лиса','Кошка','Собака','Свинья']
path='D:\\Documents\\PythonTest\\pythonProject\\resources\\Pictures\\11_tasks\\11_06\\'
imgs=[PhotoImage(file=(path+f)) for f in files]


cmb = Combobox(wnd,values=animals,font=('Times New Roman',14),state='readonly')
cmb.current(0)
lbl=Label(wnd,image=imgs[0])

cmb.pack(side='top',padx=5,pady=5)
lbl.pack(side='top',padx=5,pady=5,)

def change(*args):
    animal=cmb.get()
    index=animals.index(animal)
    lbl.configure(image=imgs[index])
        
cmb.bind('<<ComboboxSelected>>',change)

wnd.mainloop()