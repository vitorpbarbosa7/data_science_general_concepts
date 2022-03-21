import unittest 
import calc

# Giving access do different capabilities from unittest.TestCase
class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result,15)

        result = calc.add(-3, 5)
        self.assertEqual(result,2)

        result = calc.add(-7, -1)
        self.assertEqual(result,-8)

        result = calc.add(0, 0)
        self.assertEqual(result,0)


    def test_subtract(self):
        result = calc.subtract(10, 5)
        self.assertEqual(result,5)

        result = calc.subtract(-3, 5)
        self.assertEqual(result,-8)

        result = calc.subtract(-7, -1)
        self.assertEqual(result,-6)

        result = calc.subtract(0, 0)
        self.assertEqual(result,0)

    
    def test_multiply(self):
        result = calc.multiply(10, 5)
        self.assertEqual(result,50)

        result = calc.multiply(-3, 5)
        self.assertEqual(result,-15)

        result = calc.multiply(-7, -1)
        self.assertEqual(result,7)

        result = calc.multiply(0, 0)
        self.assertEqual(result, 0)

    def test_divide(self):
        result = calc.divide(10, 5)
        self.assertEqual(result,2)

        result = calc.divide(-10, 5)
        self.assertEqual(result,-2)

        result = calc.divide(-7, -1)
        self.assertEqual(result,7)

        result = calc.divide(0, 1)
        self.assertEqual(result, 0)

        with self.assertRaises(Exception) as context:
            calc.divide(0, 0)
        self.assertTrue('Can not divide by zero' in str(context.exception))

        with self.assertRaises(Exception) as context:
            calc.divide(-5, 0)
        self.assertTrue('Can not divide by zero' in str(context.exception))

if __name__ == '__main__':
    unittest.main()