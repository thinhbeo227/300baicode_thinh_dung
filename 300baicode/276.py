import math 
xa,ya,xb,yb=map(int,input().split())
ab=f"{(((xa-xb)**2)+((ya-yb)**2))**0.5:.2f}"
ac = math.sqrt((xa-xb)**2 + (ya-yb)**2)
print(ab)