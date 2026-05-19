'''
kiểm tra số hoàn hảo

6: 1 2 3 --> 1 + 2 + 3 = 6 --> shh

8: 1 2 4 --> 1 + 2 + 4 = 7 != 8 --> NO

28: 1 2 4 7 14 = 28 --> YES


for i in range(1, n)
    n % i == 0:

            ton + = i

if tong == n: yes
else

'''
loncocacola1=int(input())
loncocacola2=0
for i in range(1, loncocacola1):
    if loncocacola1%i==0:
        loncocacola2+=i
if loncocacola2==loncocacola1:
    print('Yes')
else:
    print('No')