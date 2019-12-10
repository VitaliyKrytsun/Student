# import json


# with open('data.json', 'rt') as json_file:


#     json_dict = {
#         'array': [1,2,3,4],
#         'int': 1,
#         'float': 1.,
#         'str':'str'
# }

# #json_data = json.dump(json_dict, json_file)
#     print(json.load(json_file))




# class Context:
#     def __enter__(self, *args):
#         print('On open')

#     def __exit__(self, *args):
#         print('On close')

# with Context() as ctx:
#     pass

class Stack(list):
    def push(self, elem):
        self.append(elem)
        return self

    def pop(self):
        return self.pop()

    def __neg__(self):
        self.reverse()
        return self

    def __index__(self):
        return len(self)

    def __eq__(self, other):
        return len(self) == len(other)

    def __add__(self, other):
        min_len = min(len(self), len(other))
        bigger_stack = self if len(self) > min_len else other
        new_stack = Stack()
        for idx in range(min_len):
            new_stack.push(self[idx] + other[idx])
        new_stack += bigger_stack[min_len :]
        return new_stack


stack1 = Stack([1,2,3])
stack2 = Stack([4,5,6,7,8])

print(stack1 + stack2)


