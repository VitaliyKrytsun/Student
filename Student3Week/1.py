my_list = input('Введіть список:')
n = int(input('Введіть кількість максимальнтх чисел:'))
k = sorted(my_list)
k.reverse()
def maxima():
    if n == 0: 
        l = k[0]
        print(l)
    else:
        l = k[0:n]
        print(l)
maxima()
