a=input()
b=input()
c=input()
a=a.split(' ')
for i in a:
    if i == b:
        print(c,end=" ")
    else:
        print(i,end=" ")