class Stationery:

    def __init__(self, title):
        self.title = title

    def draw (self):
        print ('Запуск отрисовки')

class Pen (Stationery):
    def draw(self):
        print('Отрисовка ручкой')

class Pencil (Stationery):
    def draw(self):
        print('Отрисовка карандашем')

class Handle (Stationery):
    def draw(self):
        print('Отрисовка маркером')

pen = Pen ('pen')
pencil = Pencil ('pencil')
handle = Handle ('handle')
stationery = Stationery ('stationery')

pen.draw()
pencil.draw()
handle.draw()
stationery.draw()