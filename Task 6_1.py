import time # для реализации пауз между переключением сигналов светофор

class TrafficLight:

    __color = 0 # не понял, зачем нужет этот атрибут

    def running (green_time):
        while True:
            print ('Горит красный цвет')
            time.sleep (7)
            print('Горит желтый цвет')
            time.sleep(2)
            print('Горит зеленый цвет')
            time.sleep(int(green_time))


trafficLight = TrafficLight
trafficLight.running(5)