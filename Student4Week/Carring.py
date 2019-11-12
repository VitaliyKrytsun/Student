# curry = lambda fn, x: lambda y: fn(x, y)
# add = lambda x, y: x + y
# print(curry(add, 4)(5))   # => 9


def curry(fucn):
    def inner():
        new_curry = lambda func, x: lambda y: func(x,y)
        return sum(lambda x, y: x + y)
    return inner

@curry
def c():
    return c(4,5)

print(c)
