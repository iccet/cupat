from linalg.vector import Vector
import unittest


class VectorTestCase(unittest.TestCase):
    v_a = Vector([15, 2])
    v_b = Vector(14, 202)
    v_c = Vector([14, 202.04])

    v_ab_mul = Vector([210, 404])
    v_ab_sum = Vector([29, 204])
    v_ab_sub = Vector([1, -200])
    v_ab_div = Vector([15 / 14, 2 / 202])

    def test_str(self):
        self.assertEqual("<15, 2>", str(self.v_a))

    def test_abs(self):
        self.assertAlmostEqual(15.1327459504, abs(self.v_a))
        self.assertEqual(1, abs(self.v_a.normalized()))

    def test_eq(self):
        self.assertNotEqual(self.v_b, self.v_a)
        self.assertEqual(self.v_b, self.v_c)

        self.assertEqual(self.v_a, self.v_a)
        self.assertNotEqual(self.v_a, self.v_c)

    def test_gle(self):
        _v_zero = Vector([0, 0])
        _v_a = Vector([2, 3])
        _v_b = Vector([6, 9])
        _v_c = Vector([5, 9])

        self.assertGreaterEqual(_v_b, _v_zero)
        self.assertGreaterEqual(_v_b, _v_zero)
        self.assertGreater(_v_b, _v_zero)

        self.assertGreaterEqual(_v_a, _v_zero)
        self.assertLessEqual(_v_a, _v_b)
        self.assertGreater(_v_a, _v_zero)

        self.assertGreaterEqual(_v_b, _v_a)
        self.assertLessEqual(_v_zero, _v_a)

    def test_mul(self):
        v_res = self.v_a.copy()

        v_res = self.v_a * self.v_b
        self.assertEqual(v_res, self.v_ab_mul)

        v_res *= v_res
        self.assertEqual(v_res, self.v_a * self.v_b * self.v_a * self.v_b)

    def test_pow(self):
        v_res = self.v_a.copy()

        v_res = self.v_a ** -1
        self.assertEqual(v_res, Vector([1 / 15, 1 / 2]))

        v_res = self.v_a ** -5
        self.assertEqual(v_res, Vector([15 ** -5, 2 ** -5]))

    def test_div(self):
        v_res = self.v_a.copy()
        v_res /= self.v_a
        self.assertEqual(v_res, Vector([1, 1]))
        v_res = self.v_a / self.v_b
        self.assertEqual(v_res, self.v_ab_div)

    def test_sub(self):
        v_res = self.v_a - self.v_b
        self.assertEqual(v_res, self.v_ab_sub)
        v_res -= -self.v_b
        self.assertEqual(v_res, self.v_a)

    def test_add(self):
        v_res = self.v_a + self.v_b
        self.assertEqual(v_res, self.v_ab_sum)
        v_res += -self.v_b
        self.assertEqual(v_res, self.v_a)

    def test_matmul(self):
        _res = self.v_a @ [[1, 0], [0, 1]]
        self.assertEqual(_res, self.v_a)

        _res = self.v_a @ [[0, 0], [0, 0]]
        self.assertEqual(_res, Vector([0, 0]))


if __name__ == '__main__':
    unittest.main()
