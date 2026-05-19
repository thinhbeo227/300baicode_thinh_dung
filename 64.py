'''

for ... 1, n + 1:
    if i % 3
        s = s + 1
. 1 2 [3] 4 5 [6] ... [9]
3
'''
n=int(input())
s= 0
for i in range(1,n+1):
    if i%3==0 :
        s=s+1
print(s)
