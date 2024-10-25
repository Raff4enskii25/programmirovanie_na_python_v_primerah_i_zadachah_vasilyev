class Alpha:
    def __init__(self,val):
        self.value=val
    def __eq__(self,val): #оператор "="
        print("Alpha: 'равно'")
        return self.value==val
    def __ne__(self,val): #оператор "!="
        print("Alpha 'не равно'")
        return self.value!=val
    def __lt__(self,val): #operator "Меньше"
        print("Аlpha 'меньше'")
        return self.value<val
    def __ge__(self,val): #operator "больше или равно"
        print("Alpha 'больше или равно'")
        return self.value>=val
class Bravo:
    def __init__(self,val):
        self.value=val
    def __eq__(self,val):
        print("Bravo: 'равно'")
        return self.value==val
    
A=Alpha(100)
print("Operations with A")
print(f"[01] A==100: {A==100}")
print(f"[02] A!=100: {A!=100}")
print(f"[03] 200==A: {200==A}")
print(f"[04] 200!=A: {200!=A}")
print(f"[05] A<200: {A<200}")
print(f"[06] 200>A: {200>A}")
print(f"[07] A>=200: {A>=200}")
print(f"[08] 100<=A: {100<=A}")
B=Bravo(300)
print("Operations with B")
print(f"[09] B==300: {B==300}")
print(f"[10] B!=300: {B!=300}")
print(f"[11] 400==B: {400==B}")
print("Comparison A and B")
print(f"[12] A==B: {A==B}")
print(f"[13] B!=A: {B!=A}")
print(f"[14] A!=B: {A!=B}")

