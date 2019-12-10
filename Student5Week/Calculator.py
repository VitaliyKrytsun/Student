while True:
    s = input("Введіть знак (+,-,*,/): ")
    if s == '0': break
    if s in ('+','-','*','/'):
        x = float(input("Введіть x="))
        y = float(input("Введіть y="))
        if s == '+':
            print("Відповідь = %s " % (x+y))
        elif s == '-':
            print("Відповідь = %s " % (x-y))
        elif s == '*':
            print("Відповідь = %s " % (x * y))
        elif s == '/':
            if y != 0:
                print("Відповідь = %s " % (x/y))
            else:
                print("Ділення на нуль не можливе")
    else:
        print("Невірний знак операції!")
        