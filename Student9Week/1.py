# class Singleton(type):
#     __cls_instances = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in Singleton.__cls_instances:
#             Singleton.__cls_instances[cls] = super().__call__(*args, **kwargs)
#         return Singleton.__cls_instances[cls]




# class A(metaclass=Singleton):
#     pass

# a1 = A()
# a2 = A()

# print(id(a1) == id(a2))


class A:
    __instances = None

    def __new__(cls, *args, **kwargs):
        if A.__instances is None:
            A.__instances = super().__new__(cls, *args, **kwargs)
        return A.__instances


a1 = A()
a2 = A()

print(id(a1) == id(a2))
