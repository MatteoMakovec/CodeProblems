import unittest
from UniqueString import src


class TestSum(unittest.TestCase):
    def testing(self):
        string = "44"
        self.assertEqual(src.is_unique(string), False)


if __name__ == '__main__':
    unittest.main()
