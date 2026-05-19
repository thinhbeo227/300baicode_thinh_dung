# a     b
# 1234 56
# 4 + 5

'''
a = a % 10 = 4

b = b // 10
b = b % 10


a + b
'''
a,b=map(int,input().split())
a=a%10
b=b//10
b=b%10
print(a+b)