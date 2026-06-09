n=int(input())
TNT=0
while n !=0:
    r = n % 10 
    n = n // 10 
    if r%2==1:
        TNT=TNT+1
print(TNT)