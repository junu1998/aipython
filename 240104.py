i=1
while i<4:
    print("안녕",i)
    i+=1

    
for i in range(1, 5):
    print(f"{i} Welcome")

    for j in range(1, 4):
        print(f"{j} Hello")

print("Done")


A,B,C=map(int,input().split())
if (B<=A<=C) or (C<=A<=B):	#A가 2번째로 큰 경우
    print(A)
elif (A<=B<=C) or (C<=B<=A): #B가 2번째로 큰 경우
	print(B)
else:						#C가 2번째로 큰 경우
    print(C)


A,B,C=map(int,input().split())
nums=[A,B,C]
nums.sort()



#2차원 리스트
score = [[29, 28, 27, 30],
    [30, 20, 27, 29],
    [23, 25, 29, 30]]

for r in range(len(score)):
    for c in range(len(score[r])):
        print(score[r][c], end=" ")
    print()
