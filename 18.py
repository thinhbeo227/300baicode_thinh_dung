'''
n = 4010 
gio = 1h con dư 410s

'''

a=int(input())
gio = a // 3600
a=a%3600
phut=a//60
giay=a%60
print(f'{gio}:{phut}:{giay}')