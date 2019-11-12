class Base:
    a = 'a'
    b = 'b'
    _list = []

    # def __init__(self, **kwargs):
    #     for key in kwargs:
    #         setattr(self, key, kwargs[key])
    def __init__(self, public = None, private=None, protected=None):
        self.public = public
        self._private = private
        self.__protected = protected

    def print(self):
        print('Base')



base = Base(1, 2, 3)
print(base.public)
print(base._private)
print(base._Base__protected)
base.print()


class A(Base):
    a = 'a from A'
    def print(self):
        print('A')

class B(Base):
    def print(self):
        print('B')

class C(A, B):
    def print(self):
        super(A, self).print()
        print('C')

# a = A('a')
# a.print()
# b = B('b')
# b.print()
# c = C('c')
# c.print()
# print(C.mro())
# c.asd = 'asd'
# print(c.asd)

class D(Base):
    @staticmethod
    def mean(*args):
        return sum(args) / len(args)
    @classmethod
    def class_method(cls):
        print(cls)
d = D()
print(d.mean(1,2,3))
print(D.mean(1,2,3))
d.class_method()






# base = Base(a = 'str', b ="str b")
# print(base.a)
# print(base.b)

# print(base.a, base.b)
# print(base._list)
# base._list +=[1]

# base1 = Base()
# print(base1._list)
