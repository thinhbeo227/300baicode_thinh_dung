'''
trong gio uu tien cho dung lam
ngoai gio acc
for .. [m, n]:
    t = t + i
    d = d + 1

    if i % 7 == 0:
        d7 = d7 + 1
print(d7)

if dem == 0: 
    print(0.0)
else:
    prrint(tbc:2f)
'''
m,n=map(int,input().split())
t=0
d=0
d7=0
tbc=0
for i in range(m,n+1):
    if i%2==0 or i%3==0:
        d=d+1
        t=t+i
    if i % 7 == 0:
        d7 = d7 + 1
print(d7, end=" ")
if d==0:
    print('0.0')
else :
    tbc = t/d
    print(f"{tbc:.1f}")


