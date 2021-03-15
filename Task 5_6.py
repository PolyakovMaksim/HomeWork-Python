with open ('my_file.txt', 'r') as f:
    dictionary = {}
    for line in f:
        line_list = line.split()
        sum_hours = 0
        for el in line_list[1:]:
            if el == '-':
                hours = 0
            else:
                hours = int (el[:el.index('(')])
            sum_hours += hours
        dictionary[line_list[0][:-1]] = sum_hours
    print(dictionary)