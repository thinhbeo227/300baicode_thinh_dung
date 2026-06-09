# # a=list(map(int,input().split()))
# a = [1, 2, 3, 4, 5]
TNT=0
# for i in range(len(a)):
#     # print(a[i], end=' ')
#     if a[i] < 0:
#         TNT += 1
        
# if TNT != 0:
#     print('YES')
# else: print("NO")






a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]<0:
        TNT=TNT+1
if TNT !=0:
    print("YES")
else:
    print("NO")