def construct_dict(S):
    char_dict = {} # char_dict - словник символів
    for c in S:
        if c not in char_dict:
            char_dict[c] = S.count(c)
    return char_dict

def find_most_popular_char(D):
    max_char = '' # найпопулярніший символ
    max_num = 0 # кількість його входжень
    for c, num in D.items():
        if num > max_num:
            max_char = c
            max_num = num
    return max_char, max_num
S = input("Задайте рядок ")
D = construct_dict(S)
C, N = find_most_popular_char(D)
print("символ '%s' входить у рядок %d разів" % (C, N))