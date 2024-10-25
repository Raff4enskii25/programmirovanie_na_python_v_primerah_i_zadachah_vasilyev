from tkinter import *
from math import *
#функция для события "курсор в области рисования"
def msEnter(evt):
    cnv.itemconfig(Pct,image=img_2) #смена изображения

#функция для события "курсор покинул область рисования"
def msLeave(evt):
    cnv.itemconfig(Pct,image=img_1)
    cnv.delete("ln") #удаление "старых" линий возле курсора

#функция для события перемещения курсора в области рисования
def msMotion(evt):
    x=evt.x
    y=evt.y #координаты курсора
    cnv.delete("ln") #удаление "старых" линий
    #отображение линий
    cnv.create_line(x,5, x, H-5, fill=clr_C1, width=2, tag="ln")
    cnv.create_line(5, y, W-5, y, fill=clr_C1, width=2, tag="ln")
    Rxy=cnv.coords(Rtn) #координаты прямоугольника
    Cxy=cnv.coords(Crl) #координаты окружности
    #координаты центра окружности
    x0=(Cxy[2]+Cxy[0])/2
    y0=(Cxy[3]+Cxy[1])/2
    #расстояние от курсора до центра окружности
    r=sqrt((x-x0)**2+(y-y0)**2)
    #если курсор внутри окружности:
    if r<R:
        #белый цвет заливки окружности
        cnv.itemconfig(Crl,fill=clr_C2)
        #красный цвет заливки прямоугольника
        cnv.itemconfig(Rtn,fill=clr_C1)
        return
    #Если курсор вне окружности:
    else:
        #красный цвет для окружности
        cnv.itemconfig(Crl,fill=clr_C1)
    #Если курсор находится внутри прямоугольника
    if x>Rxy[0] and x<Rxy[2] and y>Rxy[1] and y<Rxy[3]:
        #зеленый цвет заливки прямоугольника
        cnv.itemconfig(Rtn,fill=clr_R2) 
    #Если курсор вне прямоугольника:
    else:
        #белый цвет заливки прямоугольника
        cnv.itemconfig(Rtn,fill=clr_R1)

#Функция для обработки события нажатия кнопки вверх
def msUp(evt):
    cnv.move("Lns",0,-1) #линии на 1 пиксель вверх
    cnv.move(Crl,0,3) #окружности на 3 пикселя вниз

#функция события нажатия кнопки вниз
def msDown(evt):
    cnv.move("Lns",0,1)
    cnv.move(Crl,0,-3)

#Нажатие кнопки влево
def msLeft(evt):
    cnv.move(Txt,-1,0)

def msRight(evt):
    cnv.move(Txt,1,0)

W=600;H=400 #область рисования
w=200; h=100 #прямоугольник
N=10 #кол-во линий
d=20 #декремент для длины линий
R=30 #радиус окружности
fnt=("Arial",20,"bold")
txt="Синий текст"
clr="lightgreen" #цвет для линий
#цвет для области рисования
clr_1="lightyellow"
clr_2="yellow"
#цвет для закраски окружности
clr_C1="red"
clr_C2="white"
#цвет для закраски прямоугольника
clr_R1="white"
clr_R2='green'

wnd=Tk()
wnd.geometry(str(W+10)+'x'+str(H+10)+"+400+300")
wnd.title("Графика")
wnd.resizable(False, False)

cnv=Canvas(wnd,bg=clr_1,bd=3,relief=GROOVE)
cnv.place(x=5,y=5,width=W,height=H)
cnv.focus_set()

Txt=cnv.create_text(W/2,50,text=txt,font=fnt,fill="blue")

for k in range(N):
    x1=70+k*d
    y1=H/4+10*k
    x2=W-70-d*k
    y2=H/4+10*k
    cnv.create_line(x1,y1,x2,y2, fill=clr, width=5,tag="Lns")

#координаты для создания окружности
x1=W/2-R
y1=H/2-R+30
x2=W/2+R
y2=H/2+R+30
#Создание окружности
Crl=cnv.create_oval(x1,y1,x2,y2,fill=clr_C1)

#координаты для создания прямоугольника
x1=20
y1=H-h-20
x2=x1+w
y2=y1+h
#Создание прямоугольника
Rtn=cnv.create_rectangle(x1,y1,x2,y2,fill=clr_R1)

img_1=PhotoImage(file="D:\\Documents\\PythonTest\\pythonProject\\resources\\Pictures\\11_07\\sad.png")
img_2=PhotoImage(file="D:\\Documents\\PythonTest\\pythonProject\\resources\\Pictures\\11_07\\smile.png")
Pct=cnv.create_image(W-20,H-20,anchor=SE,image=img_1)

#Регистрация обработчиков
cnv.bind("<Left>",msLeft)
cnv.bind("<Right>",msRight)
cnv.bind("<Up>",msUp)
cnv.bind("<Down>",msDown)
cnv.bind("<Enter>",msEnter)
cnv.bind("<Leave>",msLeave)
cnv.bind("<Motion>",msMotion)
cnv.bind("<Button-1>",lambda evt:cnv.config(bg=clr_2))
cnv.bind("<Button-3>",lambda evt:cnv.config(bg=clr_1))

wnd.mainloop()