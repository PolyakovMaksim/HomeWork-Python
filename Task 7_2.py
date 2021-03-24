class Clothes:

    def __init__(self, param):
        self.param = param

    @property
    def __str__(self):
        pass

    def __add__(self, other):
        return f'Потребуется {"%.3f"% (self.cloth + other.cloth)} ткани.'

class Coat (Clothes):

    def __str__(self):
        self.cloth = self.param / 6.5 + 0.5
        return str("%.3f"% (self.cloth))

class Suit (Clothes):

    def __str__(self):
        self.cloth = self.param * 2 + 0.3
        return str("%.3f"% (self.cloth))

my_coat = Coat (5)
print(my_coat)
my_suit = Suit (5)
print (my_suit)
print (my_coat + my_suit)