my_list = [2, 4, 6, 46, 3, 5, 1, 7, 3, 46, 93, 5, 100]
new_list = [my_list[el] for el in range (0, len(my_list)) if my_list[el] > my_list[el-1]]
print(f'Исходный список {my_list}')
print(f'Получившийся список {new_list}')

"""
можно было бы написать 
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
но в таком случае будет некорректная обработка повторяющихся значений списка
"""