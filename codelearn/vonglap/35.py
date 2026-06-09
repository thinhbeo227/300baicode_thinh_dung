'''
a = 3
b = 7
3 4 5 6 7
'''
# dem_c = dem_le = 0

# print(f'Number of even numbers: {dem_c}')
a=int(input())
b=int(input())
dc=0
dl=0 
for i in range( a , b +1 ):
    if i % 2 ==0:
        dc=dc+1
    else:
        dl=dl+1
print(f"Number of even numbers: {dc}")
print(f"Number of odd numbers: {dl}")

'''
2 4 6 8 1 3 5 7 9 
'''