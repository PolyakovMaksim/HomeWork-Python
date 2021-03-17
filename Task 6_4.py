class Car:

    a = 0 # флаг для определения движения (стоим или едем)

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go (self):
        print('Машина поехала')
        self.a = 1

    def stop (self):
        print('Машина остановилоась')
        self.a = 0

    def turn (self, direction):
        print(f'Машина повернула {direction}')

    def show_speed (self):
        if self.a == 0:
            print ('Текущая скорость авто - 0')
        else:
            print(f'Текущая скорость авто - {self.speed}')

class TownCar (Car):

    def show_speed (self):
        if self.a == 0:
            print ('Текущая скорость авто - 0')
        else:
            print(f'Текущая скорость авто - {self.speed}')
            if self.speed > 60:
                print ('Вы превышаете скорость')

class SportCar (Car):
    pass

class WorkCar (Car):

    def show_speed (self):
        if self.a == 0:
            print ('Текущая скорость авто - 0')
        else:
            print(f'Текущая скорость авто - {self.speed}')
            if self.speed > 60:
                print ('Вы превышаете скорость')

class PoliceCar (Car):
    pass

# Далее проверка всех методов и атрибутов

opel = TownCar (70, 'white', 'astra', False)
ferrari = SportCar (120, 'red', 'roma', False)
renoulte = WorkCar (30, 'black', 'logan', False)
ford = PoliceCar (100, 'blue', 'crown_victoria', True)

print(opel.name)
opel.go()
opel.show_speed()
opel.turn ('Направо')
print('-' * 70)

print(ferrari.name)
ferrari.go()
ferrari.show_speed()
ferrari.stop()
ferrari.show_speed()
print('-' * 70)

print(renoulte.name)
renoulte.show_speed()
renoulte.go()
renoulte.show_speed()
print('-' * 70)

print(ford.name)
print( ford.name, ford.speed, ford.color, ford.is_police)