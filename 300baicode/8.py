hhh=int(input())
JJJ=int(input())
p=21*hhh+5*JJJ-2009
q=(21*hhh*hhh-5*JJJ)/(2009*JJJ*JJJ)
r=(21*hhh+5*JJJ*JJJ)/(2009*JJJ+15)
print(f"{p} {q:.4f}")

print(f"{r:.6f}")