'''
s = 1 + 2 + 3 + ... + n
'''
# s = 0 
# n = int(input())
# for i in range(1, n + 1):
#     s = s + i 
# print(s)
'''
s = 0
s = s + i = s + 1 = 1
s = s + i = s + 2 = 1 + 2
s = s + i = s + 3 = 1 + 2 + 3
...
s = 1 + 2 + .. + n
'''


# 1/2 + 2/3 + 3/4 + ... + n/n+1

# s = 0 
# n = int(input())
# for i in range(1, n + 1):
#     s = s + i / (i + 1)
# print(f'{s:.2f}')

'''
s = s + i/(i + 1) = 0 + 1/2
s = 1/2 + 2/3
s = 1/2 + 2/3 + 3/4
'''

r=int(input())
u=0
for o in range(1,r+1):
    u=u+o/(o+1)

print(f'{u:.2f}')