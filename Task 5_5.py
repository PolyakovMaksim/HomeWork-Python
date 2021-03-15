with open ('my_file.txt', 'w') as f:
    print('45 34324 363 341 14124', file = f, end='')
with open ('my_file.txt', 'r') as f:
    a = f.readline()
    b = a.split()
    y = 0
    for x in b:
        y += int(x)
    print(y)