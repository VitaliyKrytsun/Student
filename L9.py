####   list comprehention  ####
####   set comprehention  ####
####   dict comprehention  ####
####   generator expression  ####

#patern iterator sproshchuje dostup do objektu

#dlia iteratora v pythoni --- __iter__() i __next__()

####   list comprehention  ####
xs = [1, 2, 3, 4, 5, 6, 7]
negative_xs = [1, -2, 3, -4, 5, -6, 7]

l = [x**2 for x in negative_xs if x < -1]
print(l)
ll = [y**2 for y in xs for x in xs]
print(ll)

####   set comprehention  ####

# s = {1 if x > 0 else 0 for x in negativ_xs}
# print(s)

####   dict comprehention  ####

# s = {x: (1 if x > 0 else 0) for x in negative_xs}
# print(s)

### objekty iteratora ###

class Range:
    """
    Iterable class
    """
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):    ### iter maje povertaty iterator
        return RangeIterator(self.start, self.stop)

class RangeIterator:
    """
    Iterator class
    """
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __next__(self):
        if self.start < self.stop:
            tmp = self.start
            self.start += 1
            return tmp
        raise StopIteration
    def __iter__(self):
        return self

#r = iter(Range(1, 6)) ## iter dostaje z objektu joho iterator
# r = RangeIterator(1, 6)
# for i in r:
#     print(i)

# for i in r:
#     print(i)

# r = RangeIterator(1, 3)
# print(next(r))
# print(next(r))
# print(next(r))

# r = RangeIterator(1, 3)
# for i in r:
#     print(i)
# for i in r:
#     print(i)

# r = Range(1, 3)
# for i in r:
#     print(i)
# for i in r:
#     print(i)


#####  VYRAZ  GENERATOR  ####

# import sys

# g_expr = (x**2 for x in range(1000_000_000))
# print(sys.getsizeof(g_expr))   #vertaje rozmir objekta v bajtah
# g_compr = [x**2 for x in range(1000_000)]
# print(sys.getsizeof(g_compr))

# def gen():
#     counter = 10
#     while counter:
#         yield counter  #yield zaminuje return, vertajemo znachennia z generatora, + zupyniajetsia generator
#         counter -= 1

# g = gen()

# i = 0
# while i < 10:
#     print(next(g))
#     i +=1

# next(g)

# def simple_gen():
#     yield 1
#     yield 2
#     x = yield 3
#     yield x*2

# # for i in simple_gen():
# #     print(i)

# g = simple_gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(g.send('a'))

# print(dir(g))

# def inf_gen():
#     x = yield 'start'
#     while True:
#         x = yield x

# g = inf_gen()

# print(next(g))
# for i in range(10):
#     print(g.send(i))

# print(g.send(10))
# try:
#     g.close()
# except StopIteration:
#     print(next(g))

#### asynhronna funkcija  #####
# async def f():
#     ...
#     await ...

#     return ...











