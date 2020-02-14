from ._vector import Vector, Iterable, List, Iterator

Matrix = Iterable[Vector]


# noinspection PyTypeChecker
class Matrix:
    """ Matrix methods implementation
    transpose,
    det (available in SqMatrix)
    add, mul, div, matmul
    """
    _varr: List[Vector] = None  # vectors array

    def __init__(self, *args) -> Matrix:
        self._varr = [Vector(args[i]) for i in range(len(args))]

    def __str__(self):
        return "\n".join(str(i) for i in self)

    def __getitem__(self, item):
        return self._varr[item]

    def __setitem__(self, key, value):
        self._varr[key] = value

    def __iter__(self) -> Iterator[Vector]:
        for i in self._varr:
            yield i

    def __round__(self, n=None):
        self = Matrix(*map(round, self))
        return self

    def __len__(self) -> int:
        return len(self._varr)

    def __neg__(self) -> Matrix:
        return Matrix(*(-i for i in self))

    def __pos__(self) -> Matrix:
        return self

    def to_list(self) -> list:
        return list(list(i) for i in self)

    def __eq__(self, other) -> bool:
        if len(self) != len(other) or len(self[0]) != len(other[0]):
            return False
        return all(self[i] == other[i] for i in range(len(self)))

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __add__(self, other: Matrix) -> Matrix:
        return Matrix(*map(Vector._sum, self, other))

    def __iadd__(self, other: Matrix) -> Matrix:
        self._varr = list(map(Vector._sum, self, other))
        return self

    def __sub__(self, other: Matrix) -> Matrix:
        return Matrix(*map(Vector._sub, self, other))

    def __isub__(self, other: Matrix) -> Matrix:
        self._varr = list(map(Vector._sub, self, other))
        return self

    def __mul__(self, other) -> Matrix:
        return Matrix(*map(lambda x: x * other, self))

    def __imul__(self, other) -> Matrix:
        self = self * other
        return self

    def __truediv__(self, other) -> Matrix:
        return Matrix(*map(lambda x: x / other, self))

    def __itruediv__(self, other) -> Matrix:
        self = self / other
        return self

    def copy(self) -> Matrix:
        return Matrix(*self._varr.copy())

    def __copy__(self) -> Matrix:
        return self.copy()

    def __matmul__(self, other):
        n = len(self[0])
        if n != len(other):
            raise IndexError("Multiply matrix error: Incompatible matrix dimensions.")
        m = len(self)
        k = len(other[0])
        return Matrix(*[Vector(sum(self[i][p] * other[p][j] for p in range(n)) for j in range(k)) for i in range(m)])

    def __imatmul__(self, matrix):
        self = self @ matrix
        return self

    def _rows_swap(self, i, k):
        n = len(self) - 1
        if i > n or k > n:
            raise IndexError("Impossible to change non-existent rows.")
        else:
            self[i], self[k] = self[k], self[i]
            return self

    def _rows_sum(self, i, k):
        n = len(self)
        if i > n or k > n:
            raise IndexError("Impossible to change non-existent rows.")
        else:
            self[i] = Vector(self[k][j] + self[i][j] for j in range(n))
            return self

    def _row_mul(self, i, k):
        n = len(self)
        if i > n:
            raise IndexError("Impossible to change non-existent row.")
        else:
            self[i] = Vector(map(lambda j: k * j, self[i]))
            return self

    def swap_row(self, i, row):
        self[i] = Vector(row)

    @staticmethod
    def _minor(m, col, row=0):
        n = len(m[0])
        keys = [sorted([(col + p) % n for p in range(1, n)]) for j in range(1, n)]
        return [[m[j][keys[j - 1][p - 1]] for p in range(1, n)]
                for j in range(1, n)]

    def transposed(self):
        return Matrix(*[Vector(self[j][i] for j in range(len(self))) for i in range(len(self[0]))])

    def transpose(self):
        self = self.transposed()
        return self


class SqMatrix(Matrix):
    """
    """
    __E = None  # alias for unit matrix

    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def _k(i): return 1 if i % 2 == 0 else -1

    def __abs__(self) -> float:
        return self.det()

    def det(self):
        n = len(self)
        if n == 1:
            return self[0]
        elif n == 2:
            return self._2x2_det(self)
        elif n == 3:
            return self._3x3_det(self)
        else:
            return self._nxn_det(self)

    def __reversed__(self):
        d = self.det()
        m = self.__matrix_from_minors().transposed() / d
        # return m

    def __matrix_from_minors(self):
        return SqMatrix(*[Matrix._minor(self, i, j) for j in range(len(self))for i in range(len(self))])

    @staticmethod
    def _2x2_det(m):
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    @staticmethod
    def _3x3_det(m):
        n = len(m)
        return sum(
            SqMatrix._k(i) * m[0][i] * SqMatrix._2x2_det(
                Matrix._minor(m, i)
            ) for i in range(n))

    @staticmethod
    def _nxn_det(m):
        n = len(m)
        if n < 5:
            return sum(SqMatrix._k(i) * m[0][i] * SqMatrix._3x3_det(Matrix._minor(m, i)) for i in range(n))
        else:
            return sum(SqMatrix._k(i) * m[0][i] * SqMatrix._nxn_det(Matrix._minor(m, i)) for i in range(n))


def _sq_solve(m: SqMatrix, r: Vector):
    """ Cramer's rule """
    mdet = abs(m)
    tm = m.transposed()
    d = []
    for i in range(len(m)):
        m = SqMatrix(*tm)
        m.swap_row(i, r)
        d.append(SqMatrix(*m.transpose()).det())
    return [d[i] / mdet for i in range(len(m))]


def _rev_solve(m: SqMatrix, r: Vector):
    """ Reverse matrix method
    (just in case)
    """
    return


def _shared_solve(matrix: SqMatrix, res: Vector):
    """ Cramer's rule """
    mdet = abs(matrix)
    d = []
    for i in range(len(matrix)):
        m = SqMatrix(*matrix)
        for j in range(len(matrix)):
            m[i][j] = res[j]
        d.append(m.det())
    return [d[i] / mdet for i in range(len(matrix))]


def solve(matrix: SqMatrix, res: list):
    if isinstance(matrix, SqMatrix):
        return _sq_solve(matrix, res)
    else:
        _shared_solve(matrix, res)


__all__ = [
    "solve",
    "SqMatrix", "Matrix"
]
