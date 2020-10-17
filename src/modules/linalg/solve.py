from .matrix import SqMatrix, Matrix
from .vector import Vector


def solve(matrix: Matrix, res: list, **kwargs):
    method = kwargs.get("method", None)
    if method is None:
        if isinstance(matrix, SqMatrix):
            return sq_solve(matrix, res)
        else:
            return shared_solve(matrix, res)
    else:
        return method(matrix, res)


def shared_solve(matrix: Matrix, res: Vector):  # TODO matrix any size
    """ Gaussian elimination
    @type matrix: SqMatrix
    @type res: Vector
    @rtype: list
    """
    return


def reverse_solve(matrix: SqMatrix, res: Vector):
    """ Reverse matrix method
    @type matrix: SqMatrix
    @type res: Vector
    @rtype: list
    """
    return list(*(reversed(matrix) @ SqMatrix(*res)).transpose())


def sq_solve(matrix: SqMatrix, res: Vector):
    """ Cramer's rule
    @type matrix: SqMatrix
    @type res: Vector
    @rtype: list
    """
    det = abs(matrix)
    if det == 0:
        return None
    d = []
    for i in range(len(matrix)):
        m = SqMatrix(*matrix)
        for j in range(len(matrix)):
            m[j][i] = res[j]
        d.append(m.det())
    return [d[i] / det for i in range(len(matrix))]


__all__ = ["solve"]
