# def snt(n):
#     if n < 2: 
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# m, n = map(int, input().split())

# s = 0
# d = 0
# for i in range(m, n + 1):
#     if snt(i): 
#         s += i
#         d += 1

# print(f'{s / d:.1f}')


def o(n):
    if 2>n:
        return False
    for i in range(2,n): # 2 -> n - 1
        if n%i==0:
            return False
    return True
t=0
d=0        
n,m =map (int,input().split())
for i in range(n,m+1):
    if o(i):
        t=t+i
        d=d+1
print(f'{t/d:.1f}')