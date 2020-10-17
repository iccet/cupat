from typing import List, Iterator, Iterable

from .vector import Vector, T
import operator

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
        return Matrix(*map(round, self))

    def size(self) -> tuple:
        return len(self._varr), len(self._varr[0])

    def __neg__(self) -> Matrix:
        return Matrix(*(-i for i in self))

    def __pos__(self) -> Matrix:
        return self

    def __eq__(self, other: Matrix) -> bool:
        ss = self.size()
        so = other.size()
        if ss[0] != so[0] or ss[1] != so[1]:
            return False
        return all(self[i] == other[i] for i in range(ss[0]))

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __add__(self, other: Matrix) -> Matrix:
        return Matrix(*map(operator.add, self, other))

    def __iadd__(self, other: Matrix) -> Matrix:
        self._varr = list(map(operator.add, self, other))
        return self

    def __sub__(self, other: Matrix) -> Matrix:
        return Matrix(*map(operator.sub, self, other))

    def __isub__(self, other: Matrix) -> Matrix:
        self._varr = list(map(operator.sub, self, other))
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

    def copy(self) -> Matrix:
        return Matrix(*list(self._varr).copy())

    def __copy__(self) -> Matrix:
        return self.copy()

    def __matmul__(self, other):
        ss = self.size()
        so = other.size()

        n = ss[1]
        if n != so[0]:
            raise IndexError("Multiply matrix error: Incompatible matrix dimensions.")
        m = ss[0]
        k = so[1]
        return Matrix(*[Vector(sum(self[i][p] * other[p][j] for p in range(n)) for j in range(k)) for i in range(m)])

    def __imatmul__(self, matrix):
        self = self @ matrix
        return self

    def _rows_swap(self, i, k):
        size = self.size()
        n = size[0] - 1
        if i > n or k > n:
            raise IndexError("Impossible to change non-existent rows.")
        else:
            self[i], self[k] = self[k], self[i]
            return self

    def _rows_sum(self, i, k):
        size = self.size()
        n = size[0]
        if i > n or k > n:
            raise IndexError("Impossible to change non-existent rows.")
        else:
            self[i] = Vector(self[k][j] + self[i][j] for j in range(n))
            return self

    def _row_mul(self, i, k):
        size = self.size()
        if i > size[0]:
            raise IndexError("Impossible to change non-existent row.")
        else:
            self[i] = Vector(map(lambda j: k * j, self[i]))
            return self

    def swap_row(self, index, row: list):
        self[index] = Vector(row)

    def transposed(self):
        s = self.size()
        return Matrix(*[Vector(self[j][i] for j in range(s[0])) for i in range(s[1])])

    def transpose(self):
        self = self.transposed()
        return self


def cofactor(i: int, j: int) -> int:
    """ Coefficient expansion of Minors
    @param i: column index
    @param j: row index
    @return: cofactor
    @rtype: int
    """
    return 1 if (i + j) % 2 == 0 else -1


class SqMatrix(Matrix):
    """ SqMatrix methods implementation
    det
    reverse
    """
    __E = None  # alias for unit matrix

    def minor(self, col: int, row: int = 0) -> SqMatrix:
        """
        @rtype: SqMatrix
        """
        n = len(self)
        col_keys = [sorted([(col + j) % n for j in range(1, n)]) for _ in range(1, n)]
        row_keys = sorted([[(row + i) % n for _ in range(1, n)] for i in range(1, n)])
        return SqMatrix(*[[self[row_keys[i][j]][col_keys[i][j]] for j in range(n - 1)]
                          for i in range(n - 1)])

    def __init__(self, *args) -> None:
        super().__init__(*args)

    def __len__(self) -> int:
        return len(self._varr)

    def __abs__(self) -> T:
        return self.det()

    def __reversed__(self) -> SqMatrix:
        d = abs(self)
        if d == 0:
            raise ValueError
        return self.__matrix_from_minors().transpose() / d

    def __matrix_from_minors(self) -> SqMatrix:
        n = len(self)
        return SqMatrix(*[
            [cofactor(i, j) * abs(self.minor(j, i)) for j in range(n)] for i in range(n)
        ])

    def det(self) -> T:
        n = len(self)
        if n > 1:
            return sum(cofactor(i, 0) * self[0][i] * self.minor(i).det() for i in range(n))
        else:
            return self[0][0]


__all__ = ["SqMatrix", "Matrix"]
