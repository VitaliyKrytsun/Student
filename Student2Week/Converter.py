n = int(input('Введіть число:'))
c = n
h = n
x = n
#print(bin(n))
#print(bin(int(input()))[2:])
b = ''                  # Перевід в бінапну систему
while n > 0:
    b = str(n % 2) + b
    n = n // 2

a = ''                  # Перевід в 8 систему
while h > 0:
     a = str(h % 8) + a
     h = h // 8

d = hex(x)
 
print('dec'+ '    '+ 'bin'+'       '+'oct'+'   '+'hex'+"\n" + str(c)+'     '+str(b) +'     '+ str(a)+'    '+str(d)) 