n =int(input()) 
a=[]
while n  !=0:
    r = n % 10 # r = 3
    n = n // 10 # n = 12
    a.append(r)
# a = [3, 2, 1]

#### n = 0
a.reverse() # [1, 2, 3]

# duyet qua a 
print(*a)





'''
123
'''