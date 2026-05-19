n=int(input())

# n = 234
min=9
while n!=0:
    r=n%10
    if r<min:
     min=r
    n=n//10    

print(min)