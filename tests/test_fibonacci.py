from fibo import find_fibonacci
from unittest import TestCase


class FibonacciTestCase(TestCase):
    def test_fibonacci_is_number(self):
        x = find_fibonacci(5)
        self.assertIsInstance(x, int)

    def test_fibonacci_is_are_not_null(self):
        x = find_fibonacci(7)
        self.assertIsNotNone(x)

    def test_fibonacci_is_equal(self):
        x = find_fibonacci(12)
        self.assertEqual(145, x)
        x1 = find_fibonacci(2)
        self.assertEqual(1, x1)
        x2 = find_fibonacci(16)
        self.assertEqual(987, x2)
