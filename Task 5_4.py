with open ('my_file.txt', 'r') as f:
    x = ('Один','Два','Три','Четыре')
    for line in f:
        y = line.split(' - ')[1]
        with open ('my_file_2.txt', 'a') as f_2:
            print(x[int(y)-1]+ ' - '+ y, file = f_2, end='')