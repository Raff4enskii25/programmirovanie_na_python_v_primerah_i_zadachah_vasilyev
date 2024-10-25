from threading import *
from time import sleep
def display(txt):
    A=[1,2]
    B=["A","B"]
    sleep(1)
    myevent.wait() #ожидание установки флага
    myevent.clear() #отмена установки флага
    for a in A:
        print(f"[{a}] {txt}")
    myevent.set() #установка флага
    sleep(1)
    myevent.wait()
    myevent.clear()
    for b in B:
        print(f"[{b}] {txt}")
    myevent.set()
myevent=Event()
myevent.set()
F=Thread(target=display,args=["Первый"])
S=Thread(target=display,args=["Второй"])
F.start()
S.start()
F.join()
S.join()