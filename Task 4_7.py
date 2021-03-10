def fact(n):
    my_list = [el for el in range (1,n+1)]
    result = 1
    for el in my_list:
        result = result * int(el)
        yield el, result

for el, result in fact(10):
   print(f'Факториал {el}! = {result}')