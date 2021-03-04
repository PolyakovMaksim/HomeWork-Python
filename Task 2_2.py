my_list = []
result_list = []
b=''
print('Введите значения списка, после нажмите Enter, для окончания ввода введите End')
c = input()

while c != 'End':
    my_list.append(c)
    c = input()

if len(my_list) % 2 == 1:
    b = my_list.pop(-1)

for el in range(0, len(my_list), 1):
    if el % 2:
        a = my_list.pop(0)
        result_list.append(a)
    else:
        a = my_list.pop(1)
        result_list.append(a)

if b != '':
    result_list.append(b)
print(result_list)
