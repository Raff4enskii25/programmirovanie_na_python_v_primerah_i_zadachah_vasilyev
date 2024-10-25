txt = input("Введите текст: ")
num = 0
new_txt = ""
while num<len(txt)-1:
    new_txt += txt[num+1] + txt[num]
    num +=2
if num<len(txt):
    new_txt+=txt[num]
print("New text", new_txt)