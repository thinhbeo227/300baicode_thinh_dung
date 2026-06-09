"""
nam nhuan
thang: 30, 31
thang 2: 28 || 29

nam = input()
if nam % 400 == 0 || nam % 4 == 0 




"""
a, b=map(int,input().split())
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a==10 or a ==12:
    print(31)
elif a == 2:
    # kiem tra nam nhuan
    if b %400 == 0      or b%4==0  and b % 100 != 0:
        print(29)
    else:
        print(28) 
elif a == 4 or a ==6 or a==9 or a==11:
    print( 30)


    
