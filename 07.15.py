# 07.15
# def 함수 9번부터
'''
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
'''
def testPrime():
    for n in range(2,101):
        A={}
        A.approve[n]
        for i in range(2,101):
            if n != i :
                if n%i ==0:
                    remove(A[n])
        print(A)
testPrime()
























