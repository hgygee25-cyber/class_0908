 #2025.06.30
#조건문 Programming
'''
a,b = eval(input("정수 2개 입력: "))
if a%b==0:
    print("약수입니다")
else:
    print("약수가 아닙니다")

a=eval(input("현재 온도를 입력하시오: "))
if a >= 25:
    print("반바지를 추천합니다.")
else:
    print("긴바지를 추천합니다.")

a= eval(input("문자를 입력하시오: "))
if a =='R' or a=='r':
    print("Rectangle")
elif a== 'C' or a== 'c':
    print("Circle")
elif a=='T' or a=='t':
    print("Triangle")
else:
    print("Unknown")

r=eval(input("원의 반지름: "))
if r<0:
    print("잘못된 값입니다.")
else:
    wid= r*r*3.14
    print(wid)
 
a,b,c= eval(input("3개의 정수를 입력하시오: "))
if a<b and a<c:
    print(f"제일 작은 정수는 {a}입니다.")
if b<c and b<a:
    print(f"제일 작은 정수는 {b}입니다.")
if c<a and c<b:
    print(f"제일 작은 정수는 {c}입니다.")

a=("선택하시오(1:가위, 2:바위, 3:보)")
b=("컴퓨터의 선택(1:가위, 2:바위, 3:보)")
if a==b:
    print("비겼습니다")
if a>b:
    print("이겼습니다.")
if a<b:
    print("졌습니다.")
 
a=eval(input("키를 입력하시오(cm): "))
b=eval(input("나이를 입력하시오: "))
if a>= 140 and b>=10:
    print("타도 좋습니다.")
else:
    print("탑승이 불가합니다.")
 
a,b=eval(input("체중과 키를 입력하세요: "))
c=(a-100)*0.9
if c==b:
    print("표준입니다.")
if c>b:
    print("저체중입니다.")
if c<b:
    print("과체중입니다.")

import random
a=('덧', '뺄', '곱', '나')
b=random.choice(a)
c=eval(input("숫자를 입력하시오: "))
d=eval(input("숫자를 입력하시오: "))
print(b)
A= float(input("값은?"))
if b == '덧':
    if A== c+d:
        print("맞았습니다")
    else:
        print("틀렸습니다")
elif b=='뺄':
    if A== c-d:
        print("맞았습니다")
    else:
        print("틀렸습니다")
elif b=='곱':
    if A== c*d:
        print("맞았습니다")
    else:
        print("틀렸습니다")
else:
    if A== c/d:
        print("맞았습니다")
    else:
        print("틀렸습니다")
 
x=float(input("x의 값을 입력하시오: "))
if x<=0:
    a= (x**2 -9*x +2)
else:
    a = (7*x + 2)
print(a)

a=float(input("무게(kg)"))
b=float(input("키(m)"))
c= a/(b**2)
print(f"당신의 BMI는 {c}.")
if 20<=c<=24.9:
    print('정상입니다')
elif 25<=c<=29.9:
    print('과체중입니다.')
elif 30<=c:
    print('비만입니다')
else:
    print('저체중입니다')

a=int(input('연도를 입력하시오: '))
b= a%12
if b==0:
    print('원숭이띠')
elif b==1:
    print('닭띠')
elif b==2:
    print('개띠')
elif b==3:
    print('돼지띠')
elif b==4:
    print('쥐띠')
elif b==5:
    print('소띠')
elif b==6:
    print('호랑이띠')
elif b==7:
    print('토끼띠')
elif b==8:
    print('용띠')
elif b==9:
    print('뱀띠')
elif b==10:
    print('말띠')
else:
    print('양띠')

a= int(input("연도를 입력하시오: "))
if a %4==0 and a%100 !=0:
    print('윤달입니다')
elif a%400==0:
    print('윤달입니다')
else:
    print('아님')
 
a=int(input("a를 입력하시오: "))
b=int(input("b를 입력하시오: "))
c=int(input("c를 입력하시오: "))
r=b**2 - 4*a*c
if r==1:
    print(f"실근은 한개입니다.")
elif r==2:
    print(f"실근은 두개입니다.")
else:
    print('실근이 없습니다.')

a=int(input("정수 입력: "))
if a%3==0:
    print("Python")
elif a%5 ==0:
    print("Express")
elif a%3==0 and a%5==0:
    print("Python Express")
else:
    print("")
 
a=float(input("pH를 입력하시오: "))
if a<7:
    print("ACID")
elif 7<=a<8:
    print("NEUTRAL")
elif 8<=a:
    print("BASE")
  
for i in range(2,51):
    if i%2 ==0:
        print(i, end=", ")

myList= [11,22,23,99,81,93,35]
a=0
for i in range(len(myList)):
    a+=myList[i]
print(a)

a=0
for i in range(1,101):
    if i%3==0:
        a+=i
print(a)

a=int(input("정수를 입력하시오: "))
for i in range(1,a+1):
    if a%i==0:
        print(i, end=", ")
 
a=eval(input("정수를 입력하세요: "))
for i in range(1,a+1):
    print()
    for j in range(1, i+1):
        print(j, end=" ")

for i in range(1,10):
    print()
    for j in range(1,10):
        print(i*j, end=" ")
 
a=int(input("값을 입력하시오: "))
b=0
for i in range(1,a+1):
    b+=i**2
print(b)

a,b = eval(input('정수 두개를 입력하시오(크기가 작은거 먼저): '))
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        c = i
print(c)

def peri(radius):
    area=3.14*radius**2
    return area
print(peri(4.0))
'''
def




 

















