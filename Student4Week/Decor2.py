import time
# def teg_b(func):
#     def inner(*args, **kwargs):
#         return f'<b>{func(*args, **kwargs)}</b>'
#     return inner

# def teg_i(func):
#     def inner(*args, **kwargs):
#         return f'<i>{func(*args, **kwargs)}</i>'
#     return inner

# def teg_u(func):
#     def inner(*args, **kwargs):
#         return f'<u>{func(*args, **kwargs)}</u>'
#     return inner

# @teg_u
# @teg_i
# @teg_b
# def func1():
#     return "Hello"


# print(func1())

# def plus_c(func):
#     def inner (a,b,c):
#         return func(a,b) + c
#     return inner


# @plus_c
# def a_b(a,b):
#     return a + b

# print(a_b(1,2,3))


def bench(func):
    def inner(n):
        start = time.time()
        tmp = func(n)
        print(f'func({n}) takes about {time.time() - start}s')
        return tmp
    return inner


@bench
def fib(n):
    l = [0, 1]  
    if 0 < n < 2:
       return l[n]
    for _ in range(2, n):
        l.append(l[-1] + l[-2])
    
    return l[-1]


    


print(fib(2000))
print(fib(2000))

