import unittest
import LevenshteinDistance.src.solution as sol


class TestSum(unittest.TestCase):
    def testing(self):
        s1 = ""
        s2 = ""
        self.assertTrue(sol.levenshtein_distance(s1, s2))


if __name__ == '__main__':
    unittest.main()
