def show(txt: str="Функция Show()")-> None:
    print(txt)

show("Текст")
show()

print("Словарь аннотаций:", show.__annotations__)

for k in show.__annotations__:
    print(k,"-", show.__annotations__[k])

print("-"*15)

def show2(txt: str,
          num: str) -> int:
    print(f"Текст: {txt} под номером {num}")
    num2 = num*2
    return num2

print(show2("Дефолтный текст", 1))

print("Словарь аннотаций 2:", show2.__annotations__)