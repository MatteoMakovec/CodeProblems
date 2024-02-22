import unittest
import UniqueString.src.solution as sol


class TestSum(unittest.TestCase):
    def testing(self):
        string = "44"
        self.assertFalse(sol.is_unique(string))


if __name__ == '__main__':
    unittest.main()
