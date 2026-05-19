def k(n):
    a=1
    for i in range(1,n+1):
        a= a*i
    return a
# b=list(map(int,input().split())) # 5 1 4 3 2
# for i 


# '''
# 3
# 11
# 2
# 97
# n = ...
# a = []
# for i in range(n):
#     a.append(input())
    
# n = int(input())
# a = [int(input()) for i in range(n)]
# '''

# a = [i * i for i in range(3)]
# print(a)

n = int(input()) # 5
a = [int(input()) for i in range(n)]


for i in range(n):
    print(k(a[i]),end=(' '))