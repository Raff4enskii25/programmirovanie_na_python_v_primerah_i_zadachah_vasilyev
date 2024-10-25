from threading import Thread
from time import sleep
def alpha():
    for k in range(5):
        sleep(1.5)
        print(f"[{k+1}] Alpha")
def bravo():
    for k in range(5):
        print(f"[{k+1}] Bravo")
        sleep(1)
t=Thread(target=bravo)
t.start()
alpha()