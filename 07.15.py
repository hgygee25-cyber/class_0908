a= int(input("첫번째 정수를 입력: "))
b= int(input("두번째 정수를 입력: "))
if a == b:
    print(f"{a}와 {b}는 같으므로 최대공약수는 {a}가 된다.")
elif a!= b:
    if a<b:
        for i in range(1, a+1):
            if a %i ==0:
                i==i
        print(i)

    else:
        for i in range(1, b+1):
            if b %i ==0:
                i==i
        print(i)

























