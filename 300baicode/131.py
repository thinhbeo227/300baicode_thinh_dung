import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

cnt = 0
# for x in a:
#     if x % 5 == 0:
#         cnt += 1

# print(cnt)
for i in range(n):
    if a[i] % 5 == 0:
        cnt += 1

print(cnt)