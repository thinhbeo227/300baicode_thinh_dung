'''

...
7: 1 7 -> 2 --> yes

if dem == 2:
    print(yes)
else: no
'''

n=int(input())
dem=0
for i in range(1,n+1):
    if n%i==0:
        dem=dem +1
if dem ==2:
    print("Yes")
else:
    print("No")
