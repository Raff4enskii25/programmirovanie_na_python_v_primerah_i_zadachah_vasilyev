from tkinter import *
from tkinter.messagebox import *
class MyApp:
    def __init__(self):
        self.setValues() #настройка параметров
        self.makeMainWindow() #создание главного окна
        self.setVars() #определение "переменных" для обработки собтий
        self.makeMainMenu() #создание главного меню
        self.makeToolBar() #создание панели инструментов
        self.makeFrame() #создание вспомогательной панели
        self.makePopupMenu() #создание контекстного меню
        self.apply() #вычисление параметров шаблонного текста
        self.traceVars() #режим отслеживания "переменных"
        self.showMainWindow()
    
    def setValues(self):
        self.W=500
        self.H=200
        self.h=40
        self.position=str(self.W)+'x'+str(self.H)
        self.fonts=['Times New Roman', 'Arial', 'Courier New']
        self.colors={'red':'Красный','blue':'Синий','black':'Черный'}
        self.style=[['bold','Жирный'],['italic','Курсив']]
        self.imgFiles=['exit.png','bold.png','italic.png','normal.png']
        self.path='D:\\Documents\\PythonTest\\pythonProject\\resources\\Pictures\\11_06\\'
        self.font=('Courier New',10,'bold')

    def makeMainWindow(self):
        self.wnd=Tk()
        self.wnd.title('Определяем шрифт')
        self.wnd.geometry(self.position)
        self.wnd.resizable(False,False)
    
    def showMainWindow(self):
        self.wnd.mainloop()
    
    def makeMainMenu(self):
        #создание пунктов меню
        self.menubar=Menu(self.wnd)
        self.mFont=Menu(self.wnd,font=self.font,tearoff=0)
        self.mStyle=Menu(self.wnd,font=self.font,tearoff=0)
        self.mColor=Menu(self.wnd,font=self.font,tearoff=0)
        self.mAbout=Menu(self.wnd,font=self.font,tearoff=0)
        #заполнение пунктов меню
        self.setMenuFont(self.mFont)
        self.setMenuStyle(self.mStyle)
        self.setMenuColor(self.mColor)
        #заполнение последнего пункта пеню
        self.mAbout.add_command(label='О программе',command=self.showDialog)
        self.mAbout.add_separator #добавление разделителя
        self.mAbout.add_command(label='Выход',command=self.clExit)
        #добавление пунктов меню на панель меню
        self.menubar.add_cascade(label='Шрифт',menu=self.mFont)
        self.menubar.add_cascade(label='Стиль',menu=self.mStyle)
        self.menubar.add_cascade(label='Цвет',menu=self.mColor)
        self.menubar.add_cascade(label='Программа',menu=self.mAbout)
        #задаем главное меню для окна
        self.wnd.config(menu=self.menubar)
    
    def makeToolBar(self):
        mt=[self.clExit,self.clBold,self.clItalic,self.clNormal]
        self.toolbar=Frame(self.wnd,bd=3,relief=GROOVE)
        self.imgs=[]
        self.btns=[]
        for f in self.imgFiles:
            self.imgs.append(PhotoImage(file=self.path+f))
            #создание кнопки
            self.btns.append(Button(self.toolbar, image=self.imgs[-1]))
            #добавление кнопки на панель
            self.btns[-1].pack(side='left',padx=2,pady=2)
        #обработчики для кнопок
        for k in range(len(mt)):
            self.btns[k].configure(command=mt[k])
        #создание текстовой метки
        self.lblSize=Label(self.toolbar,text='Размер шрифта:',font=self.font)
        #размещение метки на панели
        self.lblSize.pack(side='left',padx=2,pady=2)
        #создание спиннера
        self.spnSize=Spinbox(self.toolbar, from_=15,to=20,font=self.font,
            width=3,justify='right',textvariable=self.size)
        #размещение спиннера на панели
        self.spnSize.pack(side='left',padx=2,pady=2)
        #размещение панели в окне
        self.toolbar.place(x=3,y=3,width=self.W-6,height=self.h)
    
    def makeFrame(self):
        self.frame=Frame(self.wnd,bd=3,relief=GROOVE)
        #создание метки и добавление ее на панель
        Label(self.frame,text='Пример текста:',font=self.font).pack(side='top')
        #создание метки для отображения шаблонного текста
        self.lblText=Label(self.frame,textvariable=self.text,relief=GROOVE,bg='white',height=5)
        #размещение метки на вспомогательной панели
        self.lblText.pack(side='top',fill='both',padx=1,pady=1)
        #размещение вспомогательной панели в окне:
        self.frame.place(x=3, y=self.h+9, width=self.W-6, height=self.H-self.h-12)
    
    def makePopupMenu(self):
        #создание объекта контекстного меню
        self.popup=Menu(self.wnd,tearoff=0,font=self.font)
        #добавление команд в контекстное меню
        self.setMenuFont(self.popup)
        #добавление разделителя
        self.popup.add_separator()
        self.setMenuStyle(self.popup)
        self.popup.add_separator()
        self.setMenuColor(self.popup)
        self.popup.add_separator()
        #добавление команды в контекстное меню
        self.popup.add_command(label='Выход',command=self.clExit)
        #определение обработчика события для котекстного меню
        self.wnd.bind("<Button-3>", lambda evt:self.popup.tk_popup(evt.x_root,evt.y_root))
    
    def setMenuFont(self,menu):
        for f in self.fonts:
            menu.add_radiobutton(label=f,value=f,variable=self.name)
        self.name.set(self.fonts[0])

    def setMenuStyle(self,menu):
        for k in range(len(self.style)):
            menu.add_checkbutton(label=self.style[k][1],onvalue=True,offvalue=False, variable=self.bi[k])
        self.bi[0].set(True)
        self.bi[1].set(False)

    def setMenuColor(self,menu):
        for r in self.colors.keys():
            menu.add_radiobutton(label=self.colors[r],value=r,
                variable=self.color)
        self.color.set('blue')
        
    def apply(self,*args):
        clr=self.color.get()
        nm=self.name.get()
        sz=self.size.get()
        #Применение цвета к метке:
        self.lblText.configure(fg=clr)
        #Список с параметрами шрифта:
        fnt=[nm,sz]
        #Формирование шаблонного текста и определения
        #параметров шрифта:
        txt=self.colors[clr]+" шрифт "+nm+"\n"
        for k in range(len(self.style)):
            if self.bi[k].get():
                fnt.append(self.style[k][0])
                txt+=self.style[k][1].lower()+" "
        txt+="размера "+str(sz)
        #применение шрифта к метке
        self.lblText.configure(font=fnt)
        #Задаем текст для метки
        self.text.set(txt)

    def setVars(self):
        self.text=StringVar()
        self.name=StringVar()
        self.bi=[BooleanVar(),BooleanVar()]
        self.size=IntVar()
        self.color=StringVar()

    def traceVars(self):
        mt=self.apply
        self.name.trace('w',mt)
        self.color.trace('w',mt)
        for k in range(len(self.bi)):
            self.bi[k].trace('w', mt)
        self.size.trace('w',mt)
    
    #Методы для кнопок
    def clExit(self):
        self.wnd.destroy()

    def clBold(self):
        self.bi[0].set(not self.bi[0].get())
    
    def clItalic(self):
        self.bi[1].set(not self.bi[1].get())
    
    def clNormal(self):
        self.bi[0].set(False)
        self.bi[1].set(False)

    def showDialog(self):
        showinfo("О программе", "Очень простая программа")

MyApp()