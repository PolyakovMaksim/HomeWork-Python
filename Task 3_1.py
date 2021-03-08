def div (a,b):
    if a.isdigit() and b.isdigit():
        a = float(a)
        b = float (b)
        if b == 0:
            print("Деление на 0 невозможно.")
        else:
            print(f"Результат деления: {a/b:.5}.")
    else:
        print("Введено не число.")
a = input('Введите делимое: ')
b = input('Введите делитель: ')
div(a,b)