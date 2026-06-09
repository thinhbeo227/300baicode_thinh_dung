a=input()
n=input()
dem=0
# for i in range(len(a)):
#     if a[i]==n:
#         dem=dem+1
for x in a:
    if x == n:
        dem += 1
print(dem)