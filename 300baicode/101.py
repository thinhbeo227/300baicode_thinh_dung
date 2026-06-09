'''
bản chất của việc in ra (*) i lần
for i in range(1, i + 1):
    print('*', end = '')
'''

'''
*
**
***
...

*****
'''

# dòng thứ i có i dấu * 
# dong thu 1 co 1 dau *
# dong thu 8 co 8 dau *

e=int(input())
for i in range(1, e + 1):
    print("*"*i)

