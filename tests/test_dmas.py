import unittest

from dmas import sum, mul, sub


class TestSum(unittest.TestCase):
    def test_sum_returns_sum_of_two_integers(self) -> None:
        self.assertEqual(sum(1, 2), 3)

    def test_mul_returns_product_of_two_integers(self) -> None:
        self.assertEqual(mul(2, 3), 6)    

    def test_sub_returns_difference_of_two_integers(self) -> None:
        self.assertEqual(sub(5, 3), 2)
        

if __name__ == "__main__":
    unittest.main()
