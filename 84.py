'''
n = int(input()) # n = 123
a = []
while n != 0:
    r = n % 10
    a.append(r) # thêm hàng đơn vị vào mảng
    n = n // 10
# mảng lúc này là [3, 2, 1]
a.reverse() # đảo ngược mảng # [1, 2, 3]
for x in a:
    print(x, end=' ')
'''
coca=int(input())
pepsi=[] # (*)
while coca != 0:
    bup=coca%10
    pepsi.append(bup)
    coca=coca//10


pepsi.reverse()
for uia in pepsi:
    print(uia,end=" ")








