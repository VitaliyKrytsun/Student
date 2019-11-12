x = ['a','a','a','b','c','c','c','c','d']

print(max(zip((x.count(item) for item in set(x)), set(x))))