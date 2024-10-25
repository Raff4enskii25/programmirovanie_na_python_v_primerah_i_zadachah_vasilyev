#9. Напишите программу, в которой открывается окно с полем ввода 
# и меткой. В поле вводится выражение (в соответствии с правилами языка
#  Python — например, алгебраическое выражение), а в метке отображается
#  значение этого выражения. Используйте функцию eval() и обработку 
# исключительных ситуаций.
from tkinter import *
wnd=Tk()
wnd.resizable(False,False)
wnd.geometry('350x200')
wnd.title('Задание 9')

equation=StringVar()

def calculate(*args):
    try:
        rslt=eval(equation.get())
        result.configure(text=rslt,bg='lightgreen')
        frm.configure(bg='lightgreen')
    except ZeroDivisionError:
        result.configure(text='На ноль делить нельзя!',bg='lightcoral')
        frm.configure(bg='lightcoral')
    except:
        result.configure(text='Введите выражение!',bg='lightcoral')
        frm.configure(bg='lightcoral')

guide_lbl=Label(wnd,text='Введите выражение:',font=('Times New Roman',16,'bold'))
txt_box=Entry(wnd,font=('Times New Roman',12,'italic'),textvariable=equation)
btn=Button(wnd,text='Вычислить',font=('Times New Roman',14,'bold'),command=calculate,bg='lightgray')
frm=Frame(wnd,bd=3,relief=GROOVE)
result=Label(frm,text='Здесь будет ваш результат',font=('Times New Roman',14,'bold'))

guide_lbl.pack(side='top',padx=5,pady=5,fill='x')
txt_box.pack(side='top',fill='x',padx=5,pady=10)
btn.pack(side='top',padx=5,pady=5)
frm.pack(side='bottom',padx=5,pady=10,expand=True,fill='x')
result.pack()

wnd.mainloop()