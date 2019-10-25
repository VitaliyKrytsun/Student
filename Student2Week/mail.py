p1 = input("Почта:")
p2 = input("Підтвердження:")
s1 = p1.split()
s1 = ''.join(s1)
s2 = p2.split()
s2 = ''.join(s2)
if s1==s2:
    print('Ok')
else:
    print('Не вірні дані')