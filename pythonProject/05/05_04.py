txt = 'Hello, Python!'
print("Текст в обратном порядке:", txt[::-1])
print("Первое слово в тексте:", txt[:5])
print("Последнее слово в тексте:", txt[7:])

new_txt = ""
delta = ord("a") - ord("A")
for s in txt:
    #Если буква в диапазоне от a до z:
    if ord(s) in range(ord("a"), ord("z")+1):
        s=chr(ord(s)-delta)
    new_txt +=s
print(new_txt)