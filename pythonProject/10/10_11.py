from threading import Thread
from time import sleep
class MyClass:
    def __init__(self,text):
        self.text=text
    def __call__(self,count,time):
        for k in range(count):
            sleep(time)
            print(f"[{k+1}], {self.text}")
print("Начинается выполнение программы")
obj=MyClass("Дочерний поток")
t=Thread(target=obj,kwargs={"time":2,"count":5})
t.start()
MyClass("Главный поток")(3,1.5)
if t.is_alive():
    t.join()
print("Программа завершила выполнение")
