def get_sum(*n, text="Сумма чисел:"):
    s=sum(n)
    print(text, end=" ")
    for i in n: 
        print(i,end=" ")
    print(f"равна {s}")

get_sum(5,4,3,2,1,10,5,5)
get_sum(1,2,3,4,5, text="Здравствуйте")