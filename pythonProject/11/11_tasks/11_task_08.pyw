# 8. Напишите программу, в которой с помощью главного меню можно 
#выбирать название животного, и картинка с этим животным отображается в окне.
from tkinter import *
wnd=Tk()
wnd.resizable(False,False)
wnd.geometry('400x350')
wnd.title('Задание 8')

animal=StringVar()

files=['fox.png','cat.png','dog.png','pig.png']
animals=['Лиса','Кошка','Собака','Свинья']
path='D:\\Documents\\PythonTest\\pythonProject\\resources\\Pictures\\11_tasks\\11_06\\'
imgs=dict((animals[files.index(f)],PhotoImage(file=(path+f))) for f in files)

lbl=Label(wnd,image=imgs['Лиса'])
lbl.pack(side='top',fill='both',padx=5,pady=5)

menubar=Menu(wnd,tearoff=0)
animal_menu=Menu(wnd,tearoff=0)
menubar.add_cascade(label='Животные',menu=animal_menu)

for i in imgs:
    animal_menu.add_radiobutton(label=i,value=i,variable=animal)

def change(*args):
    lbl.configure(image=imgs[animal.get()])

animal.trace('w',change)

wnd.config(menu=menubar)
wnd.mainloop()
