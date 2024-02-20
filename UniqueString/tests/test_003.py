import unittest
import UniqueString.src.solution as sol


class TestSum(unittest.TestCase):
    def testing(self):
        string = "asdfghjklqwertyuiop4bvcz34nvfhje"
        self.assertEqual(sol.is_unique(string), False)


if __name__ == '__main__':
    unittest.main()
