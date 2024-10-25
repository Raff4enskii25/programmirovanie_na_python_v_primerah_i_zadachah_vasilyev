from threading import *
from time import sleep
def calc(txt, op):
    global number
    for k in range(3):
        mylock.acquire()
        print(txt,": ресурс заблокирован",sep="")
        try:
            print(txt,"прочитано:",number)
            val=number
            sleep(1)
            if op:
                number=val+1
            else:
                number=val-1
            print(txt, " записано:",number)
        finally:
            print(txt,": ресурс разблокирован",sep="")
            print("-"*15)
            mylock.release()
        sleep(1)
number=0
mylock=Lock()
A=Thread(target=calc, args=["A", True])
B=Thread(target=calc, args=["B", False])
A.start()
B.start()
A.join()
B.join()