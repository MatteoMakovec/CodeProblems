import unittest
import UniqueString.src.solution as sol


class TestSum(unittest.TestCase):
    def testing(self):
        string = "asdfghjklpoiuytrewqzxcvbnm"
        self.assertTrue(sol.is_unique(string))


if __name__ == '__main__':
    unittest.main()
