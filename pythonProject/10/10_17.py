from threading import *
from time import sleep
def mysum(n,N):
    res=0
    for k in range(N+1):
        res+=k**n
        sleep(0.1)
    return res
def display(n,N):
    mylock.acquire()
    t=current_thread()
    print("Поток:", t.name)
    print("Слагаемых:",N)
    print("Степень:",n)
    print("Сумма:", mysum(n, N))
    print("-"*15)
    mylock.release()
mylock=Lock()
names=['Alpha','Bravo','Charlie','Delta']
T=[Thread(target=display, args=[k+1,10],name=names[k]) for k in range(len(names))]
for t in T:
    t.start()
for t in T:
    t.join()