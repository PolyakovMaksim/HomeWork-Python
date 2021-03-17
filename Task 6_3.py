class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        self.full_name = self.name + ' ' + self.surname
        print(f'Полное имя сотрдника - {self.full_name}')

    def get_total_income(self):
        self.total_income = self.income['wage'] + self.income['bonus']
        print(f'Полный доход сотрдника - {self.total_income}')


maxim = Position('Max', 'Polyakov', 'analitics', 40000, 20000)
maxim.get_full_name()
maxim.get_total_income()
print(maxim.name, maxim.surname, maxim.income, maxim.income['wage'], maxim.position )