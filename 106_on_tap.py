import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# Solution code here
w=int(input())
dem=0
for i in range(1,w+1):
    if w%i ==0 :
        dem=dem+1


if dem==2:
    print("Yes")
else:
    print('No')


'''
6

1 2 3  4 5 6

6 % 1 == 0 ???
'''