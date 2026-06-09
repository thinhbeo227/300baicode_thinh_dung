
cot,dong=map(int,input().split())
c=input()
for i in range(cot):
    print(c,end="")
print()

for i in range(dong-2):
    for j in range(cot):
        if j ==0 or j==cot-1:
            print(c,end="")
        else:print(" ",end="")
    print()



for i in range(cot):
    print(c,end="")
    
'''
*
**
***
****
*****
'''
