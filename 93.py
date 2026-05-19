n=int(input())
m=-1 # n = 246
while n!=0:
    r=n%10
    if r % 2 == 1 and m<r:
        # thang_gioi_nhat = r
        m=r
    n=n//10
if m==-1:
    print('-')
else:
    print(m)

