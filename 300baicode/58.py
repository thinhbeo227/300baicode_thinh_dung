a=input()
dem=0
for i in a:
    if int(i)%2==1:
        print(i , end =" ")
        dem=dem+1
if dem==0:
   print("-")