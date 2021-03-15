with open ('my_file.txt', 'r') as f:
    c = 0
    total = 0
    for line in f:
        a = line.split()
        if int(a[1]) > 20000:
            print(f'{a[0]} получает зарплату больше 20000.')
        c += 1
        total += int(a[1])
    print(f'Средняя зарплпта - {total/c}')