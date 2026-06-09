uia = input()
if 'a'<= uia <='y' or 'A' <= uia <='Y':
    print(chr(ord(uia) + 1))
elif uia=='z':
    print('a')
elif uia=='Z':
    print('A')