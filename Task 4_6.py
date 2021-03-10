from itertools import count, cycle

# 1-й скрипт
a = input('Сгенерируется 10 чисел начиная с введенного числа: ')
for i in count(int(a),1):
    if i > int(a)+9:
        break
    else:
        print(i)


# 2-й скрипт
b = ['red', 'green', 'blue', 'orange', 'black', 'white']
counter = 0
print(f'Набор значений из списка {b}')
for x in cycle(b):
    if counter == len(b):
        break
    else:
        print(x)
        counter += 1