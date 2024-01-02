#변수 선언 및 초기화
number = 10

#변수 값 변경
number = 20

#변수를 사용한 계산
result = number*2

#변수 값 출력
print(result)


a=int(input("당신의 나이는?"))
msg=str(a)+"살 이군요."
print(msg)
print("내년엔",a+1,"살이 되네요")
print(type(a))


a="파이썬"
print(a,"아 반가워")
print("%s아 반가워"%a)
msg=a+"아 반가워"
print(msg)


name="홍길동"
age=20.5
print("이름은 {:10s}이고 나이는 {:.2f}입니다.".format(name,age))