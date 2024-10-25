#Ax=B
#x = B/А. При B!=0 уравнение решений не имеет,
#а при B=0 решением явл. любое число
def solve(A,B):
    try:
        a=float(A)
        b=float(B)
    except:
        raise ValueError("Неверный формат данных")
    if a==0:
        if b!=0:
            raise ArithmeticError("Решений нет")
        else:
            raise Warning("Решение - любое число")
    return b/a
print("* Решаем линейные уравнения:")
A=[2.5,2,"три",10,0,0.0]
B=[3.0,4,0,"пять",5,0]
for k in range(len(A)):
    a=A[k]
    b=B[k]
    print(f"[{k+1}] Уравнение: {a}*x={b}")
    try:
        print("x =", solve(a,b))
    except ValueError as error:
        print("Неприятная ситуация №1")
        print(error)
    except ArithmeticError as error:
        print("Неприятная ситуация №2")
        print(error)
    except Warning as error:
        print("Неприятная ситуация")
        print(error)
print("* Все уравнение решены")