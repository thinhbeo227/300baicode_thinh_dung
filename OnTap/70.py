n=int(input())
d=0
c=0
# for i in range(1,n+1):
#     # if i%5==0 and i%3==0:
#     if i % 15 == 0:
#         d=d+1
#         c=c+i

# 15 30 45
for i in range(15, n + 1, 15):
    d = d + 1
    c = c + i
if d==0:
    print(0.0)
else:
    print(f'{c/d:.1f}')


'''
(3, 5) nguyen to cung nhau
'''