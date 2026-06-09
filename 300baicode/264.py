def hp(ep):
    return ep == ep[::-1]


ui = int(input())
a = []
for i in range(ui):
    a.append(input())
    
# a = [input() for i in range(ui)]


for i in a:
    if hp(i):
        print("YES")
    else:
        print("NO")
