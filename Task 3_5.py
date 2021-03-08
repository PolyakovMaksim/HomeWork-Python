res = 0
while exit:
    a = input('Введи числа через пробел, для выхода введите Q:')
    b = a.split ( )
    for el in b:
        if el.upper() != 'Q':
            res += float(el)
        else:
            exit = False
    print (res)