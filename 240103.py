#조건문
a = 10

if a > 5:
    print("a는 5보다 큽니다.")
print("end")


gender='M'

if gender=='M':
    print("남자입니다.")
else:
    print("여자입니다.")


score=int(input("점수를 입력하시오"))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")


a = 10
b = 5

if a > 5:
    if b < 10:
        print("a는 5보다 크고 b는 10보다 작습니다.")

if a > 5 and b < 10:
    print("a는 5보다 크고 b는 10보다 작습니다.")


#반복문
a = [1, 2, 3, 4, 5]

for i in a:
    print(i, end='')

for i in range(1, 10, 2):
    print( i )

for i in range(10):
    print(i)


#함수
def add(x,y):
    s = x + y
    a = s / 2
    return s, a

h,a = add(10,20)
print("합:",h, "평균:", a)