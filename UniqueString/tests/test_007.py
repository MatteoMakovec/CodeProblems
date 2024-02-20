import unittest
from UniqueString import src


class TestSum(unittest.TestCase):
    def testing(self):
        string = "159"
        self.assertEqual(src.is_unique(string), True)


if __name__ == '__main__':
    unittest.main()
