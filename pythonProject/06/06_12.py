def mysum(n):
    if n==0:
        return 0;
    else:
        return n+mysum(n-1)

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def show(t):
    if len(t)==0:
        print("|")
    else:
        print("|", t[-1], end="", sep="")
        show(t[:-1]) #передается срез до предпоследнего элемента

print("Сумма чиссел от 1 до n)",mysum(5))
for k in range(15):
    print(fib(k+1), end=" ")
print()
show("Hello Python")
show([1,2,3,4,5])