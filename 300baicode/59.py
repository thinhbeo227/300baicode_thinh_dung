g=input()
a=0
b=0
# '1''2'
for i in g:
    if int(i) % 2 == 0:
        a=a+int(i) # chuyen i -> int
        b=b+1
if b<1:
    print("-")
else :
    print(a)