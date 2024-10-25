#10. Напишите программу, в которой отображается окно с областью для 
#рисования. В центре области находится окружность. При нажатии кно
#пок «вверх», «вниз», «влево» или «вправо» окружность начинает дви
#гаться к одному из углов области рисования.
from tkinter import *
wnd=Tk()
wnd.resizable(False,False)
wnd.geometry('550x400')
wnd.title('Задание 10')

cnv=Canvas(wnd,bg='lightyellow',width=530,height=380,bd=3,relief=GROOVE)
cnv.pack(padx=5,pady=5)
cnv.focus_set()

R=30
x1=530/2-R
y1=380/2-R
x2=530/2+R
y2=380/2+R
circle=cnv.create_oval(x1,y1,x2,y2,fill='red')

def mvLeft(evt):
    cnv.move(circle,-5,0)
def mvRight(evt):
    cnv.move(circle,5,0)
def mvUp(evt):
    cnv.move(circle,0,-5)
def mvDown(evt):
    cnv.move(circle,0,5)

cnv.bind("<Left>",mvLeft)
cnv.bind("<Right>",mvRight)
cnv.bind("<Up>",mvUp)
cnv.bind("<Down>",mvDown)

wnd.mainloop()