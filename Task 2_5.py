my_list = [8, 6, 5, 5, 4, 4, 2, 2, 2, 0]
new_top = int(input('Введите значение, которое будет добавлено в рейтинг:'))

b = 0

for a in my_list:
    if a >= new_top:
        b += 1

my_list.insert(b, float(new_top))

print(my_list)