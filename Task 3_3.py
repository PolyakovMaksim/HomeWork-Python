def my_func(a, b, c):
    d = a + b + c - min(a, b, c)
    return d
print(my_func(1, 2, 3))