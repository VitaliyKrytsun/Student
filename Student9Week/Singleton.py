# metaclass
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

# class
# class A:
#     __instances = None

#     def __new__(cls, *args, **kwargs):
#         if A.__instances is None:
#             A.__instances = super().__new__(cls, *args, **kwargs)
#         return A.__instances


# a1 = A()
# a2 = A()

# print(id(a1) == id(a2))


# decorator

def Singleton(cls):
    objs_dict = {}
    def wrapper(*args, **kwargs):
        if cls not in objs_dict:
            objs_dict[cls] = cls(*args, **kwargs)
        return objs_dict
    return wrapper

@Singleton
class A():
    pass

a1 = A()
a2 = A()

print(id(a1) == id(a2))
print(type(A))
