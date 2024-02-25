import unittest
import PalindromePermutation.src.solution as sol


class TestSum(unittest.TestCase):
    def testing(self):
        s1 = "cdcc"
        self.assertFalse(sol.has_palindrome_permutation(s1))


if __name__ == '__main__':
    unittest.main()
