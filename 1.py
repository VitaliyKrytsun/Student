def add_three():
    """Вернуть 3 + число, введенное пользователем."""
    number = int(input('Enter a number: '))
    return number + 3
z = add_three
print(z)