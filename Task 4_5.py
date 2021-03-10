from functools import reduce

my_list = [el for el in range (100,1001, 2)]
print(f'Все четные числа от 100 до 1000: {my_list}')

def prod (a,b):
    c = int(a)*int(b)
    return c
d = reduce (prod, my_list)

print (f'Результат умножения всех четных числел от 100 до 1000 = {d}.')
