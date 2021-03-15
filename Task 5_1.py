with open ('my_file.txt', 'w') as f:
    enter = 'a'
    while enter != '':
        enter = input ('Введите строку, для выхода Enter:')
        f.writelines(enter+ '\n')