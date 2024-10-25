from threading import Thread
from time import sleep
def display(count,time,text):
    for k in range(count):
        sleep(time)
        print(f"[{k+1}], {text}")
print("Начинается выполнение программы")
t=Thread(target=display, args=(5,2,"Дочерний поток"))
t.start()
display(3,1.5, "Главный поток")
t.join()
print("Программа завершила выполнение")