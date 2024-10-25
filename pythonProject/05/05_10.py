txt = input("Введите текст: ")
new_txt = ""
min_s = ord("а")
max_s = ord("я")
min_S = ord("А")
max_S = ord("Я")

for i in txt:
    k = ord(i)
    if (k in range(min_s,max_s)) or (k in range(min_S, max_S)):
        i = chr(ord(i)+1)
    elif k==max_S:
        i = chr(min_S)
    elif k==max_s:
        i = chr(min_s)
    new_txt +=i
print(new_txt)