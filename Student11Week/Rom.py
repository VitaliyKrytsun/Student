n1 = int(input('Введіть перше число = '))
n2 = int(input('Введіть друге число = '))
Z = str(input('Введідь дію(+, -, *, /)'))

class Add():
    def __init__(self, argument):
        self.argument = argument

    def __add__(self, other):
        return other + self.argument
R1 = Add(n1)
R2 = Add(n2)
Radd = R1 + R2

class Sub():
    def __init__(self, argument):
        self.argument = argument

    def __sub__(self, other):
        return other - self.argument
R1 = Sub(n1)
R2 = Sub(n2)
Rsub = R1 - R2

class Mul():
    def __init__(self, argument):
        self.argument = argument

    def __mul__(self, other):
        return other * self.argument
R1 = Mul(n1)
R2 = Mul(n2)
Rmul = R1 * R2

class Floordi():
    def __init__(self, argument):
        self.argument = argument

    def __floordiv__(self, other):
        return other // self.argument
R1 = Floordi(n1)
R2 = Floordi(n2)
Rfloordiv = R1 // R2

def int_to_roman (integer):
       returnstring=''
       table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
       for pair in table:
           while integer-pair[1]>=0:
               integer-=pair[1]
               returnstring+=pair[0]
       return returnstring
         
if Z == '+':
    print(int_to_roman(Radd))
elif Z == '-':
    print(int_to_roman(Rsub))
elif Z == '*':
    print(int_to_roman(Rmul))
elif Z == '/':
    print(int_to_roman(Rfloordiv))
else: print('Помилка знака')






