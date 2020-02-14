from ._vector import Vector, Iterable, List, Iterator, T

Matrix = Iterable[Vector]
SqMatrix = Matrix


# noinspection PyTypeChecker
class Matrix:
    """ Matrix methods implementation
    transpose,
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

    def to_list(self) -> list:
        return list(list(i) for i in self)

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
        if i > len(self):
            raise IndexError("Impossible to change non-existent row.")
        else:
            self[i] = Vector(map(lambda j: k * j, self[i]))
            return self

    def swap_row(self, index, row: list):
        self[index] = Vector(row)

    def transposed(self):
        return Matrix(*[Vector(self[j][i] for j in range(len(self))) for i in range(len(self[0]))])

    def transpose(self):
        self = self.transposed()
        return self


class SqMatrix(Matrix):
    """ SqMatrix methods implementation
    det
    reverse
    """
    __E = None  # alias for unit matrix

    @staticmethod
    def _minor(m, col, row=0):
        n = len(m)
        col_keys = [sorted([(col + j) % n for j in range(1, n)]) for i in range(1, n)]
        row_keys = sorted([[(row + i) % n for j in range(1, n)] for i in range(1, n)])
        return [[m[row_keys[i][j]][col_keys[i][j]] for j in range(n - 1)]
                for i in range(n - 1)]

    @staticmethod
    def _k(i):
        return 1 if i % 2 == 0 else -1

    @staticmethod
    def _2x2_det(m):
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    @staticmethod
    def _3x3_det(m):
        n = len(m)
        return sum(
            SqMatrix._k(i) * m[0][i] * SqMatrix._2x2_det(
                SqMatrix._minor(m, i)
            ) for i in range(n))

    @staticmethod
    def _nxn_det(m):
        n = len(m)
        if n < 5:
            return sum(SqMatrix._k(i) * m[0][i] * SqMatrix._3x3_det(SqMatrix._minor(m, i)) for i in range(n))
        else:
            return sum(SqMatrix._k(i) * m[0][i] * SqMatrix._nxn_det(SqMatrix._minor(m, i)) for i in range(n))

    def __init__(self, *args) -> SqMatrix:
        super().__init__(*args)

    def __abs__(self) -> T:
        return self.det()

    def __reversed__(self) -> SqMatrix:
        d = abs(self)
        if d == 0:
            return None
        return self.__matrix_from_minors().transpose() / d

    def __matrix_from_minors(self) -> SqMatrix:
        n = len(self)
        return SqMatrix(*[
            [SqMatrix._k(i + j) * abs(SqMatrix(*SqMatrix._minor(self, j, i))) for j in range(n)] for i in range(n)
        ])

    def det(self) -> T:
        n = len(self)
        if n == 1:
            return self[0][0]
        elif n == 2:
            return self._2x2_det(self)
        elif n == 3:
            return self._3x3_det(self)
        else:
            return self._nxn_det(self)


def _shared_solve(matrix: Matrix, res: Vector):
    """ Gaussian elimination """
    return


def _rev_solve(matrix: SqMatrix, res: Vector):
    """ Reverse matrix method """
    return list(*(reversed(matrix) @ SqMatrix(*res)).transpose())


def _sq_solve(matrix: SqMatrix, res: Vector):
    """ Cramer's rule """
    mdet = abs(matrix)
    if mdet == 0:
        return None
    d = []
    for i in range(len(matrix)):
        m = SqMatrix(*matrix)
        for j in range(len(matrix)):
            m[j][i] = res[j]
        d.append(m.det())
    return [d[i] / mdet for i in range(len(matrix))]


def solve(matrix: Matrix, res: list, **kwargs):
    method = kwargs.get("method", None)
    if method is None:
        if isinstance(matrix, SqMatrix):
            return _sq_solve(matrix, res)
        else:
            return _shared_solve(matrix, res)
    else:
        return method(matrix, res)


solve_methods = {
    "reverse_matrix": _rev_solve,
    "cramer_rule": _sq_solve,
    "gauss": _shared_solve
}

__all__ = [
    "solve", "solve_methods",
    "SqMatrix", "Matrix"
]
