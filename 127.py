a=int(input())
n=list(map(int,input().split()))

cnt = 0

for i in range(0,a):
    if n[i]%2==1:
        cnt += 1
        print(n[i])

if cnt == 0: print('-')