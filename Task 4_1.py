from sys import argv
script_name, hours_worked, rate, prize = argv
salary = int(hours_worked)*int(rate)+int(prize)
print(f'Человек отработавший {hours_worked} часов по ставке {rate}, с премией {prize}, заработает {salary}.')