import random

def random_dec(func):
    def inner():
        rand1 = func()
        rand2 = func()
        return abs(rand1 + rand2) / 2
    return inner

@random_dec    
def get_random():
    return (random.random() - 0.5)*10

for _ in range(10):
    print(get_random())
