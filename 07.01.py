#2025.07.01
#함수 Programming
'''
def get_peri(radius = 5.0):
    r=radius**2*3.14
    print(r)
get_peri(4.0)

def plus(a,b):
    print(a+b)
def nus(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def sub(a,b):
    print(a/b)

a=int(input("첫 번째 정수를 입력하시오: "))
b=int(input("두 번째 정수를 입력하시오: "))
plus(a,b)
nus(a,b)
mul(a,b)
sub(a,b)
 
def calc(a,b):
    A=a+b
    B=a-b
    C=a*b
    D=a/b
    print(f"{A,B,C,D}가 반환되었습니다.")
a=int(input("첫 번째 정수를 입력하시오: "))
b=int(input("두 번째 정수를 입력하시오: "))
calc(a,b)
 
def score(a):
    if a >=90:
        print("A")
    elif a>=80:
        print("B")
    elif a>=70:
        print("C")
    elif a>=60:
        print("D")
    else:
        print("F")
a=int(input("점수를 입력하시오: "))
score(a)

def checkPass(p):
    A=[]
    for i in range(len(p)):
        if p[i].isupper():
            A.append(p[i])
            
        if len(A) > 0 and len(p)>=8:
            print("사용할 수 있습니다.")
            break
        if len(A) ==0 or len(p)<8 :
           p =  input("사용할 수 없습니다. 다시 입력하세요.")

a= input("패스워드를 입력하시오: ")
checkPass(a)
 
def math_problem(a,b):
    B=input(f"{a}와 {b}의 합은?")
    A=a+b
    if A != B:
        print("틀렸습니다!!")
    else:
        print("정답입니다")

a = int(input("첫 번째 정수를 입력하시오: "))
b = int(input("두 번째 정수를 입력하시오: "))
math_problem(a,b)
 
def getInRange(a,b):
    while True:
        if a > 12 or a<1:
            a=int(input("월을 입력하시오.(1부터 12사이의 값)"))
        else:
            if b>21 or b<0:
                b=int(input("일을 입력하시오.(1부터 31일 사이의 값)"))
            if a==2 and b>28:
                b=int(input("일을 입력하시오.(1부터 31일 사이의 값)"))
            else:
                print(f"입력된 날짜는 {a}월 {b}입니다.")
                break

print("날짜를 입력하세요(월과 일)")
a=int(input("월을 입력하시오.(1부터 12사이의 값)"))
b=int(input("일을 입력하시오.(1부터 31일 사이의 값)"))
getInRange(a,b)

def getMoneyText(amount):
    if amount >= 1000:
        print("1000이상의 숫자는 불과합니다.")
        return

    k = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    p = ['백', '십', '원']

    result = ''

    # 백의 자리
    hundreds = amount // 100
    if hundreds != 0:
        result += k[hundreds - 1] + p[0] + ' '

    # 십의 자리
    tens = (amount % 100) // 10
    if tens != 0:
        result += k[tens - 1] + p[1] + ' '

    # 일의 자리
    ones = amount % 10
    if ones != 0:
        result += k[ones - 1] + p[2]
    else:
        if amount == 0:
            result += '영원'
        elif tens != 0 or hundreds != 0:
            result += p[2]  # 일의 자리가 0이라도 '원'은 붙임

    print(result.strip())

amount=int(input("1000미만의 숫자를 쓰시오: "))
getMoneyText(amount)
'''
9번 할 차례








