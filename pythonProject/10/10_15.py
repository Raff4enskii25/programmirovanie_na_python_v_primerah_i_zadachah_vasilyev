from threading import *
from time import sleep
def mysum():
    global num
    k=1
    txt=str(num)
    while myevent.is_set():
        num+=k
        txt+=" + "+str(k)
        print(f"[{k}] {txt} = {num}")
        k+=1
        sleep(0.3)
print("Cумма целых чисел")
t=Thread(target=mysum)
num=0
myevent=Event()
myevent.set()
t.start()
sleep(2)
myevent.clear()
if t.is_alive():
    t.join()
print("Результат:", num)