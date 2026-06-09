j97=int(input())
a=[      ]
while j97 != 0:
    r = j97 % 10 # r = 3
    j97 = j97 // 10 # n = 12  
    if r%2==0:
        a.append(r)
a.reverse()
if len(a)==0:
    print("-")
else:print(*a)