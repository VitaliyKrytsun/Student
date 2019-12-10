class IntField:
    def __get__(self, instance, owner):
        return f"{instance.__dict__[self.name]}"

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('negative value')
        instance.__dict__[self.name] = value
    
    def __set_name__(self, owner, name):
        self.name = name



class Product:
    price = IntField()
    guantity = IntField()

    def __init__(self, price, guantity):
        self.price = price
        self.guantity = guantity


    # def __init__(self, price, guantity, name):
    #     if price < 0:
    #         raise ValueError('negative price')
    #     if guantity < 0:
    #         raise ValueError('negative guantity')

    #     self.price = price
    #     self.guantity = guantity
    #     self.name = name

p1 = Product(999, 10)

print(p1.price)
print(p1.guantity)


def f(self, x):
    print(x)

p1.f = f.__get__(p1)
p1.f(123)
p1.f(456)






# attrs_plus = {'x': 0, 'y': 0}

# class Parent:
#     def print_self(self):
#         print('Parent')


# class Meta(type):
#     _instante = None


#     def __new__(meta, name, bases, attrs):
#         if meta._instance is None:
#             attrs.update(attrs_plus)
#             meta.instance = type(name, bases + (Parent,), attrs)
#         return meta.instance

        
    



# class A(metaclass = Meta):
#     pass

# a = A()
# b = A()
# print(A.__mro__)
# print(a.y)
# print(id(a) == id(b))

import json

json_data = '{"id": 1, "obj": {"inner_id": 0}, "lst": [0, 1, 2]}'
print(json.loads(json_data))
