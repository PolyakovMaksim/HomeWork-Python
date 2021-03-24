class Matrix:

    def __init__(self, object):
        self.object = object

    def __str__(self):
        b = ('')
        for line in self.object:
            for el in line:
                b = f'{b} {el}'
            b = b + '\n'
        return b

    def __add__(self, other):
        obj = []
        for i in range(len(self.object)):
            raw = []
            for j in range(len(self.object[i])):
                raw.append(self.object[i][j] + other.object[i][j])
            obj.append(raw)
        return Matrix(obj)



mat_1 = Matrix ([[1,2,3],[4,5,6],[7,8,9]])
mat_2 = Matrix ([[5,5,5],[3,3,3],[1,1,1]])
print(mat_1+mat_2)
