def gtln(a,b):
    if a>b:
        return a
    return b
x,y,z,n=map(int,input().split())
a= gtln(x,y)
b= gtln(z,n)
if a==b:
    print('=')
else:print(gtln(a,b))