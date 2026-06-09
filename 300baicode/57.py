'''
if a > 0 and b > 0:
    Day la 2 kich thuoc cua mot hinh chu nhat
    cv = ..
    dt =  ..
else: # error
    Day khong phai la 2 kich thuoc cua mot hinh chu nhat
    if a < 0 and b < 0:
        a va b la so am
    else 
        if a < 0: "a la so am
        if b < 0: .
'''
a,b=map(int,input().split())
if a>0 and b>0:
    print('Day la 2 kich thuoc cua mot hinh chu nhat')
    print((a+b)*2,a*b)
    
else:
    print('Day khong phai la 2 kich thuoc cua mot hinh chu nhat')
    if a<0 and b<0:
        print('a va b la so am')
    elif a<0:
        print('a la so am')
    else:
        print("b la so am")