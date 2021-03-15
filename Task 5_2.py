with open ('my_file.txt', 'r') as f:
    print(f'В файле', f.name, ' количество строк =', len(f.readlines()))
    f.seek(0)
    a=0
    for line in f:
        a += 1
        print(f'В',a,'-й', 'строке',len(line.split()), 'слов(а)')