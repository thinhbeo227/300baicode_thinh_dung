# a=int(input())
# n=0
# tui = []
# while a !=0:
#     r = a % 10
#     if r % 2 == 0:
#         tui.append(r)
#     a = a//10
# tui.reverse()
# print(tui) # dung for duyet
a=int(input())
m=0
ui=[]
while a !=0:
    t=a%10
    if a%2==0:
        ui.append(t)
    a=a//10
ui.reverse()
for x in ui:
      print(x,end=" ")