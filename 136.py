
# def snt(n):
#     if n < 2: 
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True 


# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
# dem = 0
# for i in range(n):
#     if snt(a[i]):
#         dem += 1
#         print(a[i], end=' ')
# if dem == 0:
#     print("-")
def snt(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
dem=0
for i in range(n):
    if snt(a[i]):
        dem =dem+1
        print(a[i],end=" ")
if dem==0:
    print('-')
    