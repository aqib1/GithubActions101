import unittest

from dmas import sum


class TestSum(unittest.TestCase):
    def test_sum_returns_sum_of_two_integers(self) -> None:
        self.assertEqual(sum(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
