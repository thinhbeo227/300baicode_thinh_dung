n = int(input())
arr = list(map(int,input().split()))

k = int(input())
x = int(input())

arr[k] = x
for i in range(0,n):
    print(arr[i])