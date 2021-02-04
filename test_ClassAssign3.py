import unittest
import ClassAssign3

class CalcTester(unittest.TestCase):
    def test_addition(self):
        result = ClassAssign3.addition(4, 2)
        self.assertEqual(result, 6)

    def test_subtract(self):
        result = ClassAssign3.subtract(4, 2)
        self.assertEqual(result, 2)


    def test_multiply(self):
        result = ClassAssign3.multiply(4, 2)
        self.assertEqual(result, 8)


    def test_divide(self):
        result = ClassAssign3.divide(4, 2)
        self.assertEqual(result, 2)


    def test_divide2(self):
        result = ClassAssign3.divide(4, 0)
        self.assertEqual(result, 0)

    if __name__ == "__main__":
        unittest.main()
