import unittest
import UniqueString.src.solution as sol


class TestSum(unittest.TestCase):
    def testing(self):
        string = "181"
        self.assertEqual(sol.is_unique(string), False)


if __name__ == '__main__':
    unittest.main()
