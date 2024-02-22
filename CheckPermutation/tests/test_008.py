import unittest
import CheckPermutation.src.solution as sol


class TestSum(unittest.TestCase):
    def testing(self):
        s1 = "asf "
        s2 = " fas"
        self.assertTrue(sol.is_permutation(s1, s2))


if __name__ == '__main__':
    unittest.main()
