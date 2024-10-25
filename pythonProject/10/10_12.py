from threading import Thread
from time import sleep
class MyThread(Thread):
    def __init__(self,count,time,text):
        super().__init__()
        self.count=count
        self.time=time
        self.text=text
    def run(self):
        for k in range(self.count):
            sleep(self.time)
            print(f"[{k+1}] {self.text}")
print("Начинается выполнение программы")
A=MyThread(5,2,"Alpha")
B=MyThread(3,1.5,"Bravo")
A.start()
B.start()
if A.is_alive():
    A.join()
if B.is_alive():
    B.join()
print("Программа завершила выполнение")