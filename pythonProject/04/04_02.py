import random
random.seed(666)
A=set()
count = 10
while len(A)<count:
    A.add(random.randint(1,15))
print("A:"+str(A))
