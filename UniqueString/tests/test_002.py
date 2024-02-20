import unittest
import UniqueString.src.solution as sol


class TestSum(unittest.TestCase):
    def testing(self):
        string = "asdfghjklpoiuytrewqzxcvbnm"
        self.assertEqual(sol.is_unique(string), True)


if __name__ == '__main__':
    unittest.main()
