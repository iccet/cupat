from linalg.matrix import *
import unittest


class MatrixTestCase(unittest.TestCase):
    m_a = SqMatrix([15, 2, 0],
                   [88, 33, 1],
                   [76, 3, 87])
    m_b = Matrix([14, 202],
                 [34, 87],
                 [28, 9])
    m_c = Matrix([14, 202.04])

    def test_str(self):
        self.assertEqual("15 2 0\n88 33 1\n76 3 87", str(self.m_a))

    def test_neg(self):
        self.assertEqual(-self.m_a, Matrix([-15, -2, 0],
                                           [-88, -33, -1],
                                           [-76, -3, -87]))

    def test_transpose(self):
        self.assertEqual(self.m_b.transposed(), Matrix([14, 34, 28],
                                                       [202, 87, 9]))
        self.assertEqual(self.m_a.transpose(), Matrix([15, 88, 76],
                                                      [2, 33, 3],
                                                      [0, 1, 87]))

    def test_len(self):
        self.assertEqual(len(self.m_a), 3)

    def test_mul(self):
        self.assertEqual(self.m_a * 2, Matrix([2 * 15, 2 * 2, 2 * 0],
                                              [2 * 88, 2 * 33, 2 * 1],
                                              [2 * 76, 2 * 3, 2 * 87]))
        self.assertEqual(self.m_a @ self.m_b, Matrix([278, 3204],
                                                     [2382, 20656],
                                                     [3602, 16396]))
        with self.assertRaises(IndexError):
            self.m_b @ self.m_a

    def test_sum(self):
        self.assertEqual(self.m_a + Matrix([5, 2, 9],
                                           [8, 13, 1],
                                           [6, 3, 8]), Matrix([20, 4, 9],
                                                              [96, 46, 2],
                                                              [82, 6, 95]))

    def test_det(self):
        self.assertEqual(self.m_a.det(), 27860)
        self.assertEqual(SqMatrix([5, 2, 9],
                                  [8, 13, 1],
                                  [6, 3, 8]).det(), -97)

    def test_row_op(self):
        self.assertEqual(self.m_a._rows_swap(0, 1), SqMatrix([88, 33, 1],
                                                             [15, 2, 0],
                                                             [76, 3, 87]))
        self.assertEqual(self.m_a._rows_swap(0, 2), SqMatrix([76, 3, 87],
                                                             [15, 2, 0],
                                                             [88, 33, 1]))
        self.assertEqual(self.m_a._rows_sum(0, 2), SqMatrix([164, 36, 88],
                                                            [15, 2, 0],
                                                            [88, 33, 1]))
        self.assertEqual(self.m_b._row_mul(0, 2), Matrix([28, 404],
                                                         [34, 87],
                                                         [28, 9]))
        with self.assertRaises(IndexError):
            self.m_b._rows_swap(4, 1)
            self.m_b._rows_swap(3, 1)

    def test_reverse(self):
        self.assertEqual(reversed(SqMatrix([3, 2, -1],
                                           [2, -1, 5],
                                           [1, 7, -1])),
                         SqMatrix([34 / 103, 5 / 103, -9 / 103],
                                  [-7 / 103, 2 / 103, 17 / 103],
                                  [-15 / 103, 19 / 103, 7 / 103]))
        self.assertEqual(reversed(SqMatrix([5, 2],
                                           [8, 1])),
                         SqMatrix([-1 / 11, 2 / 11],
                                  [8 / 11, -5 / 11]))
        self.assertEqual(reversed(self.m_a), SqMatrix([717 / 6965, -87 / 13930, 1 / 13930],
                                                      [-379 / 1393, 261 / 5572, -3 / 5572],
                                                      [-561 / 6965, 107 / 27860, 319 / 27860]))

    def test_solve(self):
        a = SqMatrix([2, 5, 4],
                     [1, 3, 2],
                     [2, 10, 9])
        b = SqMatrix([2, 1, -1],
                     [-3, -1, 2],
                     [-2, 1, 2])
        self.assertEqual(solve(a, [30, 150, 110]), [-152, 270, -254])
        self.assertEqual(solve(b, [8, -11, - 3]), [2, 3, -1])
        self.assertEqual(solve(a, [30, 150, 110], method=solve_methods["reverse_matrix"]), [-152, 270, -254])
        self.assertEqual(solve(a, [30, 150, 110], method=solve_methods["gauss"]), [-152, 270, -254])
        self.assertEqual(solve(b, [8, -11, 3], method=solve_methods["gauss"]), [2, 3, -1])


if __name__ == '__main__':
    unittest.main()
