class Cell:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return f'Общее число клеток после сложения {self.amount + other.amount}'

    def __sub__(self, other):
        if self.amount > other.amount:
            return f'Общее число клеток после вычитания {self.amount - other.amount}'
        elif self.amount < other.amount:
            return f'Общее число клеток после вычитания {other.amount - self.amount}'
        else:
            return f'Вычитание невозможно, останется 0 клеток'

    def __mul__(self, other):
        print(f'Создана клетка с {self.amount * other.amount} ячеек')
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        print(f'Создана клетка с {int(self.amount) / int(other.amount)} ячеек')
        return Cell(int(self.amount) / int(other.amount))

    def make_order (self, raw):
        count = self.amount
        while count > raw:
            print('*' * raw, end = '')
            print('\\n', end = '')
            count -= raw
        print ('*' * count, end = '.')

cell_1 = Cell (10)
cell_2 = Cell (5)
print(cell_2+cell_1)
print(cell_2-cell_1)
cell_3 = cell_2*cell_1
cell_4 = cell_3/cell_1

cell_3.make_order(9)
