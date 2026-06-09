def lon(a,b):
    if a>b:
        return a
    else:
        return b
def nho(a,b):
    if a<b:
        return a
    else:return b
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(lon(a,b))
print(nho(c,d))
print(lon(lon(a,b),c))
print(nho(nho(a,b),nho(c,d)))