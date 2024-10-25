num = int(input("Введите число: "))
if num<0:
    num*=-1
digit=set()
if num==0:
    digit.add(0)
else:
    while num!=0:
        digit.add(num%10)
        num//=10
print("Число состоит из цифр:", digit)

digit2 = set(input("Введите число: "))
print("Число состоит из цифр:", digit2)