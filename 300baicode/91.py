n=int(input())

ko=0
while n !=0:
    u=n%10
    if ko <u:
        ko=u
    n=n//10   
print(ko)