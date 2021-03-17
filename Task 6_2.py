class Road:

    mass = 25
    thickness = 5

    def __init__ (self, _length, _width):
        self._length = _length
        self._width = _width

    def calc_all_mass (self):
        all_mass = Road.mass * Road.thickness * self._length * self._width / 1000
        print(f'Масса асфальта вашей дороги {all_mass} тонн.')

leningradka = Road (50000, 30)
leningradka.calc_all_mass()