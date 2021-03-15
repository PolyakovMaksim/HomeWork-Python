import json
with open ('my_file.txt') as f:
    dictionary_1 = {}
    dictionary_2 = {}
    counter = 0
    sum_profit = 0
    for line in f:
        line_list = line.split()
        profit = int(line_list[2]) - int(line_list[3])
        if profit > 0:
            counter += 1
            sum_profit += profit
        dictionary_1[line_list[0]] = profit
    dictionary_2 ['average_profit'] = sum_profit/counter
    my_list = [dictionary_1, dictionary_2]
with open ('json_file.txt', 'w') as f_2:
    print (my_list, file = f_2, end = '')