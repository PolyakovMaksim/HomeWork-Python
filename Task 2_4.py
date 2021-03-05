my_list = input('Введите список слов, разделенных пробелом:')

my_list = my_list.split()

b = 1  # счетчик для порядка вывода

for a in my_list:
    print(f'{b} слово в вашем списке - это {a[:10]}')
    b += 1